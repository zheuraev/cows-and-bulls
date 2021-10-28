import random
CHECK_WIN = 'LOSE'
ATTEMPTS = 0  # количество попыток


class ComputerMystery:  # класс, хранящий и загадывающий число
    def __init__(self):
        self.__my_number = '0000'  # значение загаданного числа, по умолчанию 0000

    def new_number(self):
        self.__my_number = ''.join(random.sample("0123456789", 4))  # генерация 4 значного числа с уникальными цифрами

    def get_number(self):  # функция-геттер, отдающая загаданное число
        return self.__my_number


def input_validation(input_number):  # функция проверки правильности ввода
    try:
        int(input_number)  # если будет введено не числовое значение, то функция прервется
        if len(str(input_number)) == 4:  # проверка на колличество символов в введеной строке
            return input_number
        else:
            print('Повторите ввод, должно быть целочисленное число из 4х разных цифр')
    except ValueError:
        print('Повторите ввод, не нужно писать буквами и ставить знаки препиная)')


def trying_to_guess(computer, trying, cow, bull):  # функция - попытка угадать
    mystery = computer.get_number()  # берем на проверку загаданное число
    global CHECK_WIN

    if input_validation(trying) == trying:  # првоерка на правильность ввода попытки угадать
        if mystery == trying:  # проверка на полное совпадение с загаданным числом(победу)
            CHECK_WIN = 'WIN!'
            return CHECK_WIN

        for i in range(4):  # цикл в котором подсчитываются коровы и быки
            if mystery[i] == trying[i]:
                bull += 1
            for j in range(4):
                if mystery[i] == trying[j]:
                    cow += 1
        cow = cow - bull
        return f'{bull} бык, {cow} корова'


class Game: # игровой класс, в котором описана игровая логика
    def __init__(self):
        self.computer = ComputerMystery()
        self.cow = 0
        self.bull = 0

    def game_logic(self):
        global CHECK_WIN
        global ATTEMPTS
        self.computer.new_number()  # загадываем число
        print(self.computer.get_number())  # раскомментируйте для отображения загаданного числа

        while CHECK_WIN != 'WIN!':  # игровой цикл, который закончится, когда check_win будет равен 'WIN'(игрок угадает)
            print(trying_to_guess(self.computer, input('Попытка угадать: '), self.cow, self.bull))
            ATTEMPTS += 1
        print(f'Вы угадали за {ATTEMPTS} попытки')
        ATTEMPTS = 0
        CHECK_WIN = 'LOSE' # после конца игры переопредяем переменную, что бы была возможность начать игру вновь


class UserInterface:  # игровой интерфейс, приветсвует игрока, позволяет начать игру вновь
    def __init__(self):
        self.game = Game()
        self.new_game = 'y'

    def start_game(self):
        while self.new_game == 'y':
            print('Попробуйте угадать загаданное 4х значное число(цифры не повторяются)')
            self.game.game_logic()
            self.new_game = input('Хотите сыграть еще? y/n')


def main():
    game = UserInterface()
    game.start_game()


if __name__ == '__main__':
    main()
