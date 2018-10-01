#!/usr/bin/env python
import sys
from numpy import *

def read_n(a):
    n = int(a[0])
    return a[1:n+1], a[n+1:]

def solve():
    a = map(int, sys.stdin.readline().split())
    L, t, N, C = a[:4]
    a = a[4:]
    
    d = a*(N/C) + a[:N%C]
    s = cumsum(d)*2

    try:
        maybe = (i for i in range(N) if s[i]>=t).next()
    except StopIteration:
        return s[-1]

    sub = d[maybe+1:]
    sub.append((s[maybe]-t)/2)
    sub.sort()
    sub.reverse()

    # print d
    # print s
    # print maybe
    # print sub
    return int(s[-1] - sum(sub[:L]))


if __name__=="__main__":
    T = int(sys.stdin.readline())
    for t in range(T):
        print "Case #{}: {}".format(t+1, solve())

