from __future__ import division

import os
#import sys
#from math import log, floor, ceil, sqrt, pi
#from random import randint, choice, shuffle
from collections import Counter
#from heapq import heappush, heappop, heapify
#inf = 10**20

#name = 'micro.in'
name = 'B-small-attempt1.in'

def _solve(r, y, b):
    if r < 0 or y < 0 or b < 0:
        return "IMPOSSIBLE"
    if r > y + b or y > r + b or b > r + y:
        return "IMPOSSIBLE"
    n = r + y + b
    poss = [None] * n
    pos = 0
    num = 0
    while True:
        poss[pos] = num
        pos += 2
        num += 1
        if pos >= n:
            if poss[1] == None:
                pos = 1
            else:
                break
    template = ''.join(l*c for c, l in reversed(sorted([(r, 'R'), (y, 'Y'), (b, 'B')])))
    #template = 'R' * r + 'Y' * y + 'B' * b
    res = ''.join(template[poss[i]] for i in range(n))
    counter = Counter(res)
    assert(counter['R'] == r)
    assert(counter['Y'] == y)
    assert(counter['B'] == b)
    assert(len(res) == r + y + b)
    for i in range(n):
        if not ((res[i] != res[(i+1) % n]) and (res[i] != res[(i-1+n) % n])):
            print(r, y, b, res)
            raise Exception('pruser')
    return res

def solve(*args, **kwargs):
    res = _solve(*args, **kwargs)
    return res

#solve(5, 5, 0)
#import sys
#sys.exit()

inp_path = '/home/mama/Downloads/%s'%name
if os.path.isfile(inp_path):
    os.system('mv %s .' % inp_path)
inp_file = open(name)
out_file = open('%s.out'%name, 'w')
cases = int(inp_file.readline())
for caseno in range(cases):
    (_, r, o, y, g, b, v) = tuple(map(int, inp_file.readline().split()))
    res = solve(r, y, b)
    print(caseno, res)
    print('---')
    out_file.write('Case #%d: %s\n'%((caseno+1), res))
    out_file.flush()
out_file.close()
