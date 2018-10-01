#!/usr/bin/python2
# coding: utf-8

from sys import stdin

T = int(stdin.readline().rstrip())

for ct in range(T):
    c, f, x = map(float, stdin.readline().rstrip().split())

    k = max(0, int(x/c - 2.0 / f))
    ans = x / (2.0 + k * f)
    for i in range(k):
        ans += c / (2 + i*f)

    print 'Case #{0}: {1}'.format(ct + 1, ans)
