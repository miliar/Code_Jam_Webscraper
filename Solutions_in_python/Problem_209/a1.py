import math
from itertools import combinations

def findArea(m,k):
    a = 0
    for r,h in m:
        a+=(math.pi*2*r*h)
    a+=(math.pi*m[0][0]*m[0][0])

    return a

for _ in range(int(input())):
    n, k = map(int, input().split())
    pc = []
    for __ in range(n):
        r, h = map(int, input().split())
        pc.append((r,h))

    pc.sort(reverse=True)
    combs = combinations(pc,k)

    areas = [findArea(m,k) for m in combs]
    print("Case #{}: {}".format(_+1,max(areas)))