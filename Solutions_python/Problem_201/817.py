#!/usr/bin/python

import sys

def bathroom(N, K):
    if K==1:
        return N//2, N//2-(N+1)%2
    corr = 0
    if K%2 != 0 and (N//2)*2==N:
        corr =-1
    return bathroom(N//2+corr, K//2)



with open(sys.argv[1], 'r') as f:
    cases = int(f.readline())
    for case in range(cases):
        N, K = map(int, f.readline().split())
        a, b = bathroom(N,K)
        print("Case #{:}: {:} {:}".format(case+1,a,b)) 

