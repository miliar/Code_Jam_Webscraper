#!/usr/bin/python2
# -*- coding: utf-8 -*-
# †
def solve():
    D, N = map(int, raw_input().split())
    K = [0] * N
    S = [0] * N
    for i in xrange(N):
        K[i], S[i] = map(int, raw_input().split())
    hours = [float(D - K[i]) / S[i] for i in xrange(N)]
    maxi = max(hours)
    res = D / maxi
    return res


T = int(raw_input())
for loop in xrange(T):
    res = solve()
    print 'Case #{}: {:.15f}'.format(loop+1, res)
