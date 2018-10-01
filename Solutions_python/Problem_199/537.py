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


def splitline(f):
    return map(f, readline().split())


def happy(cakes):
    return all(c == "+" for c in cakes)


def flip(cakes, start, size):
    for i in range(start, start + size):
        try:
            cakes[i] = "+" if cakes[i] == "-" else "-"
        except IndexError:
            raise Impossible


def solve():
    cakes, K = readline().split()
    K = int(K)
    cakes = list(cakes)

    flip_cnt = 0
    for i in xrange(len(cakes)):
        if cakes[i] == "+":
            continue

        flip(cakes, i, K)
        flip_cnt += 1

    return flip_cnt


def main():
    for i in xrange(int(readline())):
        try:
            res = solve()
        except Impossible:
            res = "IMPOSSIBLE"
        print_result(res, i + 1)


if __name__ == '__main__':
    main()
