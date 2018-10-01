__author__ = 'Riccardo'

import cmath
import math
import sys


INVALID_NUMBERS = [str(n) for n in range(3, 10)]


def parse_input(filename):
    with open(filename) as f:
        n_cases = int(f.readline())
        cases = []
        for row in f:
            row = row.strip()
            if row != '':
                cases.append(row.split())
        assert len(cases) == n_cases
    return cases


def find_fairs_and_squares(r):
    found = 0
    sqrt_a = math.ceil(cmath.sqrt(int(r[0])).real)
    sqrt_b = int(cmath.sqrt(int(r[1])).real + 1)
    for i in range(sqrt_a, sqrt_b):
        num = str(i)
        check = True
        if i > 9:
            for n in INVALID_NUMBERS:
                if n in num:
                    check = False
        if check:
            if check_palindrome(num) and check_palindrome(str(i ** 2)):
                # print(i)
                found += 1
    return found


def check_palindrome(num):
    size = len(num)
    for i in range(size):
        if num[i] != num[size - 1 - i]:
            return False
    return True


def check_palindrome_with_ints(num):
    exp = int(cmath.log10(num).real)
    while num > 9:
        last_digit = num % 10
        tmp = (10 ** exp)
        first_digit = int(num / tmp)
        if first_digit != last_digit:
            return False
        exp -= 2
        num -= tmp * first_digit
        num = int(num / 10)
    return True


def main():
    assert len(sys.argv) == 2
    filename = sys.argv[1]
    cases = parse_input(filename)
    with open(filename[:filename.rfind('.')] + '.out', 'wt') as f:
        for n in range(len(cases)):
            print('Case #{:d}: {:d}'.format(n + 1,
                                            find_fairs_and_squares(cases[n])),
                  file=f)


if __name__ == '__main__':
    main()