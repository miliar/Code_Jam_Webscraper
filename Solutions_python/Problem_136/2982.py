#!/usr/bin/env python

import sys


def token_stream():
    for s in sys.stdin:
        for x in s.rstrip().split():
            yield x

def get_time(n, C, F, X):
    res = 0
    for i in xrange(n + 1):
        res += C / (2.0 + i * F)
    res += X / (2.0 + (n + 1) * F)
    return res

def solve(C, F, X):
    if X <= C:
        return X / 2.0
    n = int((X * F - 2 * C) / (C * F)) - 1
    return get_time(n, C, F, X)

inp = token_stream()

T = int(next(inp))
for case in xrange(T):
    C, F, X = [float(next(inp)) for _ in xrange(3)]
    print "Case #%d: %.7f" % (case + 1, solve(C, F, X))

