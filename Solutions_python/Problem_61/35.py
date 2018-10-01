#!/usr/bin/python

import itertools
import math

MAX_N = 500
MODULE = 100003

choose = [[0 for r in range(n+2)]
          for n in range(MAX_N+1)]

choose[0][0] = 1
for n in range(1, MAX_N+1):
    for r in range(0, n+1):
        choose[n][r] = choose[n-1][r-1] + choose[n-1][r]

def calc_memo(memo):
    for n in range(2, MAX_N+1):
        memo[n] = {}
        memo[n][1] = 1
        memo[n][2] = 1
        for k in range(3, n):
            memo[n][k] = 0
            for j in range(k-1):
                if n-k-1 >= k-2-j:
                    memo[n][k] += memo[k][j+1] * choose[n-k-1][k-2-j]
                    memo[n][k] %= MODULE

def answer(memo, n):
    q = 0
    for i in range(1, n):
        q += memo[n][i]
        q %= MODULE
    return q

if __name__ == '__main__':
    memo = {}
    calc_memo(memo)
    t = int(raw_input())
    for i in range(t):
        n = int(raw_input())
        print 'Case #%d: %d' % (i+1, answer(memo, n))
