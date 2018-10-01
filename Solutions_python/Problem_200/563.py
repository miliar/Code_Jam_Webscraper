#!/usr/bin/env python

import sys
import logging

log = logging.getLogger(__name__)
logging.basicConfig()


class Impossible(Exception):
    pass


def print_result(result, i):
    sys.stdout.write("Case #%s: %s\n" % (i, result))


def readline():
    return sys.stdin.readline().rstrip('\n')


def splitline(fn=str):
    return map(fn, readline().split())


def tidy(digits):
    for i in xrange(len(digits) - 1, 0, -1):
        if digits[i] < digits[i - 1]:
            digits[i - 1] -= 1
            for j in range(i, len(digits)):
                digits[j] = 9
    return digits


def solve():
    digits = map(int, list(readline()))
    return int("".join(str(d) for d in tidy(digits)), base=10)


def main():
    for i in xrange(int(readline())):
        try:
            res = solve()
        except Impossible:
            res = "IMPOSSIBLE"
        print_result(res, i + 1)


if __name__ == '__main__':
    main()
