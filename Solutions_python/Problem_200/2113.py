#!/usr/bin/env python

import sys


def min_tidy(x):
    digits = [int(y) for y in str(x)]
    result = [0]
    for i, digit in enumerate(digits):
        if digit >= result[-1]:
            result.append(digit)
        else:
            cut = i
            result[-1] -= 1
            for j in xrange(len(result)-1, 0, -1):
                if result[j] < result[j-1]:
                    result[j-1] -= 1
                    cut = j-1
                    result.pop()
            for k in xrange(cut, len(digits)):
                result.append(9)
            break
    return int(''.join(map(str, result)))


def solve_from_input():
    case_count = int(sys.stdin.readline().strip())
    for i in xrange(1, case_count + 1):
        x = int(sys.stdin.readline().strip())
        solution = min_tidy(x)
        sys.stdout.write('Case #{}: {}\n'.format(i, solution))


if __name__ == '__main__':
    solve_from_input()

