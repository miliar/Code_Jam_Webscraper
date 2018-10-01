#!/usr/bin/python3
import math
t = int(input())

for it in range(1, t+1) :
    N, K = [int(i) for i in input().split()]
    U = float(input())
    P = [float(i) for i in input().split()]
    P = sorted(P)
    while U > 1e-6:
        nmin = 0
        minp = P[0]
        while nmin < N and P[nmin] == minp: nmin += 1
        nextp = 1
        if nmin < N: nextp = P[nmin]
        need = nmin * (nextp - minp)
        if U >= need:
            U -= need
            for k in range(nmin): P[k] = nextp
        else:
            u = U / nmin
            U = 0
            for k in range(nmin): P[k] += u
            break
    ans = 1
    for k in range(N): ans *= P[k]
    print("Case #%d:"%it, ans)