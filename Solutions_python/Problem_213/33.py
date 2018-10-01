from __future__ import division

import os
#import sys
#from math import log, floor, ceil, sqrt, pi
#from random import randint, choice, shuffle
from collections import Counter
#from heapq import heappush, heappop, heapify
#inf = 10**20

name = 'B-large.in'

def _solve(n, c, buy):
    stat = [[] for _ in range(n)]
    for p, b in buy:
        stat[p - 1].append(b)
    mx = max(Counter(b for p, b in buy).values())
    tickets = 0
    for k, bs in enumerate(stat):
        tickets += len(bs)
        mx = max(mx, tickets // (k + 1) + (1 if tickets % (k + 1) > 0 else 0))
    promotions = 0
    for bs in stat:
        promotions += max(len(bs) - mx, 0)
    return str(mx) + ' ' + str(promotions)

def solve(*args, **kwargs):
    res = _solve(*args, **kwargs)
    return res

inp_path = '/home/mama/Downloads/%s'%name
if os.path.isfile(inp_path):
    os.system('mv %s .' % inp_path)
inp_file = open(name)
out_file = open('%s.out'%name, 'w')
cases = int(inp_file.readline())
for caseno in range(cases):
    (n,c,m) = tuple(map(int, inp_file.readline().split()))
    buy = []
    for _ in range(m):
       buy.append(tuple(map(int, inp_file.readline().split())))
    res = solve(n, c, buy)
    print(caseno, res)
    print('---')
    out_file.write('Case #%d: %s\n'%((caseno+1), res))
    out_file.flush()
out_file.close()









