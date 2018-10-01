#!/usr/bin/env python

import sys


def rec(n, m):
    #print n, m
    if not n:
        return 0
    d = n % 10
    e = min(d, m)
    o = n / 10
    return e + 10 * max(rec(o, e), rec(o - o % 10 - 1, 9) if o >= 10 else -1)


def go(n):
    return max(rec(n, 9), rec(n - n % 10 - 1, 9) if n >= 10 else -1)


for i, l in enumerate(sys.stdin.read().splitlines()[1:]):
    n = int(l)
    r = go(n)
    print 'Case #%d: %d' % (i + 1, r)
