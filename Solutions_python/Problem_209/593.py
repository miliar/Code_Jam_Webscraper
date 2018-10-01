from time import time

import sys

from aks import *
from functools import cmp_to_key
from math import pi
from itertools import combinations

sys.setrecursionlimit(10000)

def memoize(function):
    cache = {}
    def decorated_function(*args):
        try:
            return cache[args]
        except KeyError:
            val = function(*args)
            cache[args] = val
            return val
    return decorated_function

def solve(P, K):
    def F(next, k):
        if 0 == k: return 0

        if next == len(P):
            return -10**100

        r, h = P[next]

        s1 = F(next + 1, k - 1)
        if s1 != -1:
            s1 = s1 + 2*r*h
        s2 = F(next + 1, k)

        if s1 > s2:
            return s1
        else:
            return s2
    F = memoize(F)

    def cmp(l, r):
        rl, hl = l
        rr, hr = r
        if rl != rr:
            return -(rl - rr)
        return -(hl - hr)


    P.sort(key = cmp_to_key(cmp))
    v = (F(i + 1, K - 1) + (P[i][0])**2 + 2*P[i][0]*P[i][1] for i in range(len(P)))
    return pi*max(v)

def input(file):
    F = open(file, "r")
    T = int(F.readline())
    for i in range(T):
        N, K = F.readline().split(" ")
        N, K = int(N), int(K)

        P = []
        for _ in range(N):
            P.append([int(e) for e in F.readline().split(" ")])

        yield i + 1, P, K

out = open("A.out", "w")

s = time()
#for (i, P, K) in input("Asample.in"):
#for (i, P, K) in input("A-small-attempt4.in"):
for (i, P, K) in input("A-large.in"):
#for (i, H, M, UV) in input("C-small-practice.in"):
#for (i, H, M, UV) in input("C-large-practice.in"):
    r = solve(P, K)
    w = "Case #%d: %.10f" % (i, r)
    print(w)
    print(w, file = out)
print("Time: %f" % (time() - s))
