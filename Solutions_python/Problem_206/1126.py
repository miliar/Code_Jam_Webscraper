#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Debuff -> Cure -> Buff -> Attack


def solve(D, N, Hk, Hs):
    slowestH = None
    Ht = {}
    for n in xrange(N):
        Ht[n] = float(D - Hk[n]) / Hs[n]
        #print ("{DBG} Ht[%d]=%f" % (n, Ht[n]))
        if ((slowestH is None) or (Ht[n] > Ht[slowestH])):
            slowestH = n
    R = D / Ht[slowestH]
    return R


T = int(raw_input())  # read a line with a single integer
for t in xrange(1, T + 1):
    D, N = [int(s) for s in raw_input().split(" ")]
    Hk = {}
    Hs = {}
    for n in xrange(N):
        Hk[n], Hs[n] = [int(s) for s in raw_input().split(" ")]
    #print ("")
    #print ("{DBG} t=%d" % (t))
    #print ("{DBG} D=%d, N=%d" % (D, N))
    #print ("{DBG} Hk=%s" % (Hk))
    #print ("{DBG} Hs=%s" % (Hs))
    print "Case #{}: {}".format(t, solve(D, N, Hk, Hs))



"""
[Python 2.x]
# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    n, m = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    print "Case #{}: {} {}".format(i, n + m, n * m)
    # check out .format's specification for more formatting options


[Python 3.x]
# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n, m = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
    print("Case #{}: {} {}".format(i, n + m, n * m))
    # check out .format's specification for more formatting options

"""
