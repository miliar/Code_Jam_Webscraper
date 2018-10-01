#!/usr/bin/python3
import math
t = int(input())

for it in range(1, t+1) :
    N, C, M = [int(i) for i in input().split()]
    C = [0] * C
    P = [0] * N
    for _ in range(M):
        p, c = [int(i)-1 for i in input().split()]
        P[p] += 1
        C[c] += 1
    ans = max(C)
    tot = 0
    for i in range(N):
        tot += P[i]
        ans2 = (tot + i) // (i+1)
        ans = max(ans, ans2)
    prom = 0
    for i in range(N-1, 0, -1):
        if P[i] > ans: prom += P[i] - ans

    print("Case #%d:"%it, ans, prom)