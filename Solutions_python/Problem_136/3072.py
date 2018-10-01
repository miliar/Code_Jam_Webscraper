#!/usr/bin/env python

import math


def time_to_win(n, c, f, x):
    return sum([c / (2.0 + k * f) for k in xrange(n)]) + x / (2.0 + n * f)


def main():
    n_tests = int(raw_input())
    for test in xrange(1, n_tests + 1):
        c, f, x = map(float, raw_input().split())
        n_farms = max(0, int(math.ceil(x / c - 2.0 / f - 1)))
        print 'Case #%d: %.7f' % (test, time_to_win(n_farms, c, f, x))


if __name__ == '__main__':
    main()
