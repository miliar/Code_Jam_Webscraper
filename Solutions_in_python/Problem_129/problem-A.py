#!/usr/bin/env python3

from heapq import *

def solve(fin, fout):
    n, m = map(int, fin.readline().split())
    cost_mem = {}
    def cost(x):
        result = cost_mem.get(x)
        if not result:
            result = ((n * x - (x - 1) * x // 2) + 1000002013) % 1000002013
            cost_mem[x] = result
        return result

    up = {}
    down = {}
    ud = set()

    original = 0
    for i in range(m):
        a, b, s = map(int, fin.readline().split())
        a -= 1
        b -= 1
        if not up.get(a):
            up[a] = 0
        if not down.get(b):
            down[b] = 0

        up[a] += s
        down[b] += s
        ud.add(a)
        ud.add(b)
        original = (original + cost(b - a) * s) % 1000002013

    tickets = []
    total = 0
    ud = list(ud)
    ud.sort()
    for i in ud:
        if up.get(i):
            tickets.append([i, up[i]])
        d = down.get(i)
        if not d: continue
        while d > 0:
            j, s = tickets[-1]
            if s < d:
                tickets.pop()
                total = (total + s * cost(i - j)) % 1000002013
                d -= s
            else:
                tickets[-1][1] -= d
                total = (total + d * cost(i - j)) % 1000002013
                break

    fout.write(str((original - total + 1000002013) % 1000002013));
    fout.write('\n');
