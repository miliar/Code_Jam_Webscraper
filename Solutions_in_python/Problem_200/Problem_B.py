import sys
import fileinput


def next_digit(number):
    reversed_digits = tuple(map(int, reversed(str(number))))
    for index in range(len(reversed_digits) - 1):
        digit = reversed_digits[index]
        if digit < reversed_digits[index + 1]:
            return index
    return -1


def wrap_digit(number, digit_index):
    reversed_number = tuple(reversed(str(number)))
    digit = int(reversed_number[digit_index])
    remainder = int("0" + "".join(reversed(reversed_number[:digit_index])))
    return number - digit * (10 ** digit_index) - remainder - 1


def solve(case):
    number = int(case)

    index = next_digit(number)
    while index != -1:
        number = wrap_digit(number, index)
        index = next_digit(number)

    return number


def main():
    with fileinput.input() as f:
        num_cases = f.readline()
        for index, case in enumerate(f, start=1):
            print("Case #{}: {}".format(index, solve(case)))


if __name__ == "__main__":
    sys.exit(main())
