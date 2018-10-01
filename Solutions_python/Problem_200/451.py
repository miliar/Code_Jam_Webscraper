#!/usr/bin/env python3 -u

import sys
from itertools import *


def parse_problems(f):
    _ = int(sys.stdin.readline())
    while True:
        line = f.readline().strip()
        if line:
            yield [int(line)]
        else:
            return


def digit_join(digits):
    return int(''.join(str(c) for c in digits))


def solve_problem(num):
    n = num
    for _ in range(2000):
        digits = [int(c) for c in str(n)]
        a, b = tee(digits, 2)

        next_idx = next(filter(
                lambda a: a[1],
                enumerate(
                    starmap(lambda x, y: y < x, zip(a, islice(b, 1, None))),
                    start=1
                )
        ), [-1, None])[0]
        if next_idx == -1:
            return n
        else:
            n -= (digit_join(digits[next_idx:]) + 1)
    else:
        raise Exception("Too many iterations for input: " + str(num))


def is_tidy(n):
    s = str(n)
    return s == ''.join(sorted(s))


def format_solution(i, solution):
    return f'Case #{i}: {solution}'


def main():
    for i, problem in enumerate(parse_problems(sys.stdin), start=1):
        print(format_solution(i, solve_problem(*problem)))


if __name__ == '__main__':
    main()