import sys
import math
import string
from heapq import heappush
from heapq import heappop

def solve(k, l):
    l.sort(key=lambda x: -x[0] * x[1])

    #res1
    m = l[:k]

    def calc_res(m):
        r_max = max([r for (r, h) in m])
        top = math.pi * r_max ** 2
        side = sum([2 * math.pi * r * h for (r, h) in m])
        return top + side
    res1 = calc_res(m)

    #res2
    l = list(l)
    l.sort(key=lambda x: -x[0])
    x = l[0]
    l = l[1:]
    l.sort(key=lambda x: -x[0] * x[1])
    m = [x] + l
    m = m[:k]
    res2 = calc_res(m)
    return max(res1, res2)

f = open('in.txt')
g = open('out.txt', 'w')
next(f)
for (i, line) in enumerate(f):
    n, k = [int(x) for x in line[:-1].split()]
    l = []
    for _ in range(n):
        line = next(f)
        r, h = [int(x) for x in line[:-1].split()]
        l.append((r, h))
    s = solve(k, l)
    s = 'Case #%s: %s\n' %(i+1, s)
    print(s)
    g.write(s)



