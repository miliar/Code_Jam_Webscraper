from unittest import TestCase, main
from math import floor, log10

def digits(number):
    return floor(log10(number)) + 1

def recicle(numbers):
    if digits(numbers[0]) != digits(numbers[1]):
        return None

    if digits(numbers[0]) == 1 or digits(numbers[1]) == 1:
        return 0

    count_recicle = 0
    for i in range(numbers[0], numbers[1]):
        for j in range(numbers[1], numbers[0] + 1, -1):
            if i >= j:
                break

            if is_recicable( (i, j) ):
                count_recicle += 1

    return count_recicle

def is_recicable(numbers):
    if str(numbers[0]) == str(numbers[1])[-1:] + str(numbers[1])[:-1]:
        return True

    if str(numbers[0]) == str(numbers[1])[-2:] + str(numbers[1])[:-2]:
        return True

    if str(numbers[0]) == str(numbers[1])[-3:] + str(numbers[1])[:-3]:
        return True

    return False

def input_file(path="input.txt"):
    input_file = open(path)

    return input_file.readlines()

def output(path):
    file_lines = input_file(path)

    repetitions = int(file_lines[0]) + 1

    output = []
    for i in range(1, repetitions):
        numbers = file_lines[i]
        numbers = numbers.split()

        numbers = (int(numbers[0]), int(numbers[1]))

        output.append("Case #" + str(i) + ": " + str(recicle(numbers)) )

    return output

class NumbersOfDigitsTestCase(TestCase):

    def test_number_1_should_have_one_digit(self):
        self.assertEqual(1, digits(1))

    def test_number_10_should_have_two_digits(self):
        self.assertEqual(2, digits(10))

class RecicleNumberTestCase(TestCase):

    def test_should_not_have_recicle_number_with_one_digit(self):
        self.assertEqual(0, recicle( (1,9) ))

    def test_should_not_have_numbers_with_diferences_count_of_digits(self):
        self.assertEqual(None, recicle( (1, 10) ))

    def test_should_12_and_21_it_recicable_numbers(self):
        self.assertEqual(True, is_recicable( (12, 21) ))

    def test_should_have_1_recicled_number_in_10_22_range(self):
        self.assertEqual(1, recicle( (10, 22) ))

    def test_should_have_3_recicled_numbers_in_10_40_range(self):
        self.assertEqual(3, recicle( (10, 40) ))

    def test_should_102_and_210_recicable_numbers(self):
        self.assertEqual(True, is_recicable( (102, 210) ))

    def test_should_have_156_recicled_numbers_in_100_500_range(self):
        self.assertEqual(156, recicle( (100, 500) ))

    def test_should_have_287_recicled_numbers_in_1111_2222_range(self):
        self.assertEqual(287, recicle( (1111, 2222) ))

    def test_should_receive_a_input_file_and_read_it(self):
        self.assertEqual(list, type(input_file()))

    def test_output_should_return_a_default_output(self):
        self.assertEqual("Case #1: 0", output(path="input_problem_c_test.txt")[0])

if __name__ == "__main__":
    main()
