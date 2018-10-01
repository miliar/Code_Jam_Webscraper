#!/usr/bin/env python

def war(naomi, ken, n):
    pos = 0
    for i in xrange(n):
        block = naomi[i]
        while pos < n and block > ken[pos]:
            pos += 1
        if pos == n:
            return n - i
        else:
            pos += 1
    return 0

def dwar(naomi, ken, n):
    score = 0
    pos = 0
    for i in xrange(n):
        block = naomi[-i-1]
        while pos < n and block < ken[-pos-1]:
            pos += 1
        if pos == n:
            return score
        else:
            score += 1
            pos += 1
    return score

for case in xrange(1, int(raw_input())+1):
    n = int(raw_input())
    naomi = sorted(map(float, raw_input().split()))
    ken = sorted(map(float, raw_input().split()))
    print "Case #%d: %d %d" % (case, dwar(naomi, ken, n), war(naomi, ken, n))
