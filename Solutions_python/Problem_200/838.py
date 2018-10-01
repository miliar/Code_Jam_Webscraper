from __future__ import division

import os
#import sys
#from math import log, floor, ceil, sqrt, pi
#from random import randint, choice, shuffle
#from collections import defaultdict
#from heapq import heappush, heappop, heapify
#inf = 10**20

name = 'B-large.in'

def _solve(n):

    def cnt():
        r = 0
        dd = 0
        for d in res:
            r *= 10
            dd = max(d, dd)
            r += dd
        return r

    length = len(str(n))
    res = [0] * length
    for i in range(length):
        for j in range(10):
            res[i] = j
            if cnt() > n:
                res[i] = j - 1
                break
    return int(''.join(map(str, res)))

def solve(*args, **kwargs):
    res = _solve(*args, **kwargs)
    return res

#print(solve(111111111111111110))
#import sys
#sys.exit(0)

inp_path = '/home/mama/Downloads/%s'%name
if os.path.isfile(inp_path):
    os.system('mv %s .' % inp_path)
inp_file = open(name)
out_file = open('%s.out'%name, 'w')
cases = int(inp_file.readline())
for caseno in range(cases):
    n = int(inp_file.readline().strip())
    res = solve(n)
    print(caseno, res)
    print('---')
    out_file.write('Case #%d: %s\n'%((caseno+1), res))
    out_file.flush()
out_file.close()
