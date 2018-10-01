#!/usr/bin/python2
# -*- coding: utf-8 -*-

import sys
import os

rl = sys.stdin.readline
def rs():
    return rl().split()

def ri():
    return int(rl())

def rvi():
    return map(int, rs())

def solve(V, X, a):
    N = len(a)
    if N == 1:
        r, x = a[0]
        if x != X:
            return "IMPOSSIBLE"
        return "%.9f" % (V / r)
    elif N == 2:
        r1, x1 = a[0]
        r2, x2 = a[1]
        if max(x1, x2) < X or min(x1, x2) > X:
            return "IMPOSSIBLE"
        if x2 == x1:
            if X != x1:
                return "IMPOSSIBLE"
            r = r1 + r2
            return "%.9f" % (V / r)
        t2 = V * (X - x1) / ((x2 - x1) * r2)
        t1 = V * (X - x2) / ((x1 - x2) * r1)
        #t1 = (V - r2 * t2) / r1
        #if t1 < -1e-11 or t2 < -1e-11:
        if t1 < 0 or t2 < 0:
        #if t1 < 0 or t2 < 0:
        #    if 0 > t1 >= -1e-11 or 0 > t2 >= -1e-11:
        #        print r1, t1, x1, "...", r2, t2, x2, "...", V, X
            return "IMPOSSIBLE"
        return "%.9f" % max(t1, t2)
    else:
        return "IMPOSSIBLE"

def main():
    T = ri()
    for t in xrange(1, T+1):
        N, V, X = rs()
        N = int(N)
        V = float(V)
        X = float(X)
        a = []
        for i in xrange(N):
            r, c = map(float, rs())
            a.append((r,c))
        print "Case #%d: %s" % (t, solve(V, X, a))


if __name__ == '__main__':
    main()
