#!/bin/env python
import sys

def s2i(s):
    if s == '.':
        return -1;
    else:
        return int(s)

def add(a,b):
    if a == -1: a = 0
    if b == -1: return a
    return a + b

def alen(a):
    c = 0
    for i in a:
        if i != -1: c += 1
    return c

def f1(a):
    if a == -1: return 0
    return a

def f2(a):
    if a == -1: return 0
    return 1

def calc(WP, OWP, OOWP):
    return 0.25 * WP + 0.50 * OWP + 0.25 * OOWP


N = int(sys.stdin.readline())

for case in xrange(N):
    print 'Case #%d:' % (case + 1) 
    T = int(sys.stdin.readline())
    R = []
    for t in xrange(T):
        #x = map(lambda a: int(a), sys.stdin.readline())
        x = sys.stdin.readline().rstrip('\n')
        l = map(lambda a: s2i(a), [x[i] for i in range(T)])
        R.append(l)
    WP = [0 for i in range(T)]
    for i in xrange(T):
        WP[i] = float(reduce(lambda a,b: add(a,b), R[i])) / float(alen(R[i]))

    OWP = [0 for i in range(T)]
    for j in xrange(T):
        for i in xrange(T):
            if R[j][i] == -1: continue
            OWP[j] += float(sum(map(lambda a: f1(a), R[i])) - f1(R[i][j])) / float(alen(R[i]) - f2(R[i][j]))
        OWP[j] /= float(alen(R[j]))

    OOWP = [0 for i in range(T)]
    for j in xrange(T):
        for i in xrange(T):
            if R[j][i] == -1: continue
            OOWP[j] += OWP[i]
        OOWP[j] /= float(alen(R[j]))

    for i in xrange(T):
        print calc(WP[i],OWP[i],OOWP[i])
    N -= 1
