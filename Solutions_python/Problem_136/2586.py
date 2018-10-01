#!/usr/bin/env python3

import sys


def solve(handle):
    data = handle.readline().split()
    c, f, x = [float(i) for i in data]
    divider, const = 2, 0
    result = x / divider
    while True:
        const += c / divider
        current = const + x / (divider + f)
        divider += f
        if current < result:
            result = current
        else:
            return result


def main(handle):
    n = int(handle.readline())
    for i in range(n):
        print('Case #{}: {}'.format(i+1, solve(handle)))


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as handle:
        main(handle)