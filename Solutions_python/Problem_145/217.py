#!/usr/bin/env python
# -*- coding: utf-8 -*-

import fractions
import math

import sys

sys.stdin.readline()

BASE = 2 ** 40
def check(b):
    while b % 2 == 0:
        b /= 2
    return b == 1

def solve(a, b):
    gcd = fractions.gcd(a, b)
    a /= gcd
    b /= gcd
    if not check(b):
        return None
    if b > BASE:
        return None

    assert BASE % b == 0
    a *= BASE / b
    return 40 - int(math.log(a, 2))

for case, line in enumerate(sys.stdin, 1):
    a, b = line.strip().split('/')
    res = solve(int(a), int(b))
    if res is None:
        res = "impossible"
    print "Case #{}: {}".format(case, res)
