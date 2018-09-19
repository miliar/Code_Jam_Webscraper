#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys, os
import operator
TEMPLATE = "Case #%d: %.6f"
def decode(r):
    A, B = [int(x) for x in r.readline().rstrip().split()]
    Aprobab = [float(x) for x in r.readline().rstrip().split()]
    return (A, B, Aprobab)

def solve(A, B, Aprobab):
    retypeNum = B + 2
    misskey = 0
    expected = retypeNum
    for i in xrange(A + 1):
        if i == A:
            result = i + B + 1
        else:
            result = calculate(A, B, Aprobab, i)
        if result < expected:
            expected = result
    return expected

def calculate(A, B, probab, misskey):
    tmpnum = 2 ** misskey
    sump = reduce(operator.mul, probab[:A - misskey])
    return (B - A + 1 + misskey * 2) * sump + (B - A + 1 + B + 1 + misskey *
        2) * (1.0 - sump)

if __name__ == "__main__":
    filename = sys.argv[1]
    with open(filename) as r:
        T = int(r.readline().rstrip())
        for i in xrange(T):
            A, B, Aprobab = decode(r)
            print TEMPLATE % (i + 1, solve(A, B, Aprobab))
