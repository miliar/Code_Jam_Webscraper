#!/usr/bin/python2
# -*- coding: utf-8 -*-
# †
def f(S, K):
    v = [ch == '+' for ch in S]
    n = len(v)
    count = 0
    for i in xrange(n):
        if v[i]:
            continue
        if i + K > n:
            return 'IMPOSSIBLE'
        count += 1
        for j in xrange(i, i+K):
            v[j] = not v[j]
    return count


T = int(raw_input())
for case in xrange(T):
    S, K = raw_input().split()
    K = int(K)
    res = f(S, K)
    print 'Case #{}: {}'.format(case+1, res)
