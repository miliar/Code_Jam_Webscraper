#!/usr/bin/env python
# -*- coding: utf-8 -*-
from IPython import embed
from numpy import binary_repr

def bin2dec(string_num):
    return str(int(string_num, 2))


def solve(n, k):
    # solve CASE 1 TODO separately
    N = int(n)
    K = str(binary_repr(int(k)))[1:]
    if int(k) == 1:
        return (N - 1) - int(N-1)//2, int(N - 1) // 2
    else:
        return rec_solver(K,N)

def rec_solver(K, N):
    if len(K) == 1:
        if int(K[0]) == 0:
            N = (N-1) - int(N-1)//2
            return (N-1) - int(N-1)//2, int(N-1)//2
        elif int(K[0]) == 1:
            N = int(N - 1) // 2
            return (N-1) - int(N-1)//2, int(N-1)//2

    else:
        if int(K[-1]) == 0:
            return rec_solver(K[:-1], (N-1) - int(N-1)//2)
        elif int(K[-1]) == 1:
            return rec_solver(K[:-1], int(N-1)//2)

if __name__ == "__main__":
    t = int(raw_input())  # read a line with a single integer
    for caseNr in xrange(1, t + 1):
        n, k = [s for s in raw_input().split(" ")]
        Max = solve(n, k)
        print("Case #%i: %s %s" % (caseNr, Max[0], Max[1]))