#!/usr/bin/env python3

import math


def read_cases():
    case_count = input()
    cases = []
    for x in range(int(case_count)):
        raw_case = input()
        cases.append(raw_case.split())
    return cases


def up(x):
    if x <= 0:
        return 0
    return 1


def pool(k):
    return int(math.pow(2, int(math.log(k, 2)) + 1))


def phi(n, x):
    return n - x + 1


def why(k):
    return int(math.pow(2, int(math.log(k, 2))))


def max_min(n, k):
    x = pool(k)
    p = phi(n, x)
    y = why(k)
    z = k - y

    division = p // x
    maximum = division + up(p % x - z)
    minimum = division + up(p % x - k)
    return maximum, minimum


def main():
    cases = read_cases()
    for i, case in enumerate(cases):
        result = max_min(int(case[0]), int(case[1]))
        print("Case #{}: {} {}".format(i + 1, result[0], result[1]))


if __name__ == '__main__':
    main()
