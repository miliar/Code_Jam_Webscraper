#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys, math, random, operator
from string import ascii_lowercase, ascii_uppercase
from fractions import Fraction, gcd
#from decimal import Decimal, getcontext
from itertools import product, permutations, combinations
from Queue import Queue, PriorityQueue
from collections import deque, defaultdict, Counter
#getcontext().prec = 100

MOD = 10**9 + 7
INF = float("+inf")

if sys.subversion[0] == "PyPy":
    import io, atexit
    sys.stdout = io.BytesIO()
    atexit.register(lambda: sys.__stdout__.write(sys.stdout.getvalue()))
    sys.stdin = io.BytesIO(sys.stdin.read())
    raw_input = lambda: sys.stdin.readline().rstrip()
pr = lambda *args: sys.stdout.write(" ".join(str(x) for x in args) + "\n")
epr = lambda *args: sys.stderr.write(" ".join(str(x) for x in args) + "\n")
die = lambda *args: pr(*args) ^ exit(0)

read_str = raw_input
read_strs = lambda: raw_input().split()
read_int = lambda: int(raw_input())
read_ints = lambda: map(int, raw_input().split())
read_float = lambda: float(raw_input())
read_floats = lambda: map(float, raw_input().split())

"---------------------------------------------------------------"

def solve(s, k):
    s = ["-+".index(c) for c in s]
    ans = 0
    for i in xrange(0, len(s)-k+1):
        if s[i] == 0:
            ans += 1
            for j in xrange(i, i+k):
                s[j] ^= 1
    if min(s) == 1:
        return ans
    return "IMPOSSIBLE"


t = read_int()
for j in xrange(t):
    d, n = read_ints()
    ans = float("+inf")
    epr(j, ":", d, n)
    for i in xrange(n):
        k, s = read_ints()
        t = (d - k) / float(s)
        ans = min(ans, d / t)
        epr(i, t, d/t)
    print "Case #%d: %.10f" % (j+1, ans)
    epr()
