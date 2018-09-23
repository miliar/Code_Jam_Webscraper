from __future__ import division

import os
#import sys
#from math import log, floor, ceil, sqrt, pi
#from random import randint, choice, shuffle
from collections import Counter
#from heapq import heappush, heappop, heapify
#inf = 10**20

name = 'A-large.in'

def _solve(p, groups):
    all_patterns = {
        2: [[0], [1, 1]],
        3: [[0], [1, 2], [1, 1, 1], [2, 2, 2]],
        4: [[0], [1, 3], [2, 2], [1, 1, 2], [3, 3, 2], [1, 1, 1, 1], [3, 3, 3, 3]]
    }
    cnts = [0] * p
    for g in groups:
        cnts[g % p] += 1
    patterns = list(map(Counter, all_patterns[p]))
    res = 0
    while True:
        found = False
        for pattern in patterns:
            if all(cnts[key] >= pattern[key] for key in pattern):
                for key in pattern:
                    cnts[key] -= pattern[key]
                found = True
                res += 1
                break
        if not found:
            break
    if sum(cnts) > 0:
        res += 1
    return res

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
    (n, p) = tuple(map(int, inp_file.readline().split()))
    groups = tuple(map(int, inp_file.readline().split()))
    res = solve(p, groups)
    print(caseno, res)
    print('---')
    out_file.write('Case #%d: %s\n'%((caseno+1), res))
    out_file.flush()
out_file.close()
