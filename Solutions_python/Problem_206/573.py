#!/usr/bin/python3

import sys
# from heapq import *

def solve(n, k):
    pass        

n_cases = int(sys.stdin.readline())

for i in range(1, n_cases+1):
    d, n = map(int, sys.stdin.readline().split())
    times = []
    for j in range(n):
        k, s = map(int, sys.stdin.readline().split())
        time = (d - k) / s
        times.append(time)
    m_time = max(times)  # Slowest horse
    annie = d / m_time
    print('Case #{0}: {1}'.format(i, annie))
