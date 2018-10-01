#!/usr/bin/env python

import os
import sys
import collections

def solve(N, K):
    cases = collections.defaultdict(int)
    for k in range(K - 1):
        if N % 2 == 0:
            cases[N / 2] += 1
            cases[N / 2 - 1] += 1
        else:
            cases[N / 2] += 2
        N = sorted(cases.keys())[-1]
        cases[N] -= 1
        if cases[N] == 0:
            del cases[N]
    if N % 2 == 0:
        return N / 2, N / 2 - 1
    else:
        return N / 2, N / 2

def main():
    T = int(sys.stdin.readline().strip())
    for t in range(T):
        N, K = map(long, sys.stdin.readline().strip().split())
        mininum, maximum = solve(N, K)
        print 'Case #%d: %d %d' % (t + 1, mininum, maximum)

if __name__ == '__main__':
    main()

