import sys
import math


def solve(D, N, horses):
    maxV = float('inf')
    for i in range(N):
        ki = horses[i][0]
        si = horses[i][1]
        maxV = min(maxV, (D/(D-ki))*si)
    return maxV


T = int(input())
for i in range(T):
    d, n = [s for s in input().split(" ")]
    D = float(d)
    N = int(n)
    horses = [[x for x in list(map(float, input().split(" ")))] for y in range(N)]
    print('Case #{}: {:f}'.format(i+1, solve(D, N, horses)))
