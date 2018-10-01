import math
from itertools import combinations

def solve(k, cakes):
    v = 0
    for i in range(len(cakes)):
        r0, h0 = cakes[i]
        rh = sorted((r*h for j, (r,h) in enumerate(cakes) if j != i and r <= r0), reverse=True)
        if len(rh) < k-1: continue
        v = max(v, math.pi*(r0**2 + 2*r0*h0 + 2*sum(rh[:k-1])))
    return v

for case in range(1, int(input())+1):
    n, k = map(int, input().split())
    cakes = []
    for _ in range(n):
        cakes.append(list(map(int, input().split())))
    answer = solve(k, cakes)
    print('Case #{}: {}'.format(case, answer))
