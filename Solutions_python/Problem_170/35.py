from __future__ import division

import os
import sys
from math import log, floor, ceil, sqrt, pi
#from random import randint, choice, shuffle
#from collections import defaultdict
#from heapq import heappush, heappop, heapify
from itertools import chain, combinations
inf = 10**20

name = 'C-small-attempt1'

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def _solve(sentences):
    ss = []
    for sentence in sentences:
        ss.append(set(sentence.split(" ")))

    english_base = ss[0]
    french_base = ss[1]
    ss = ss[2:]
    res = [inf]


    def dfs(sss, english_w, french_w):
        if len(english_w & french_w) > res[0]:
            return
        if len(sss) == 0:
            res[0] = min(res[0], len(english_w & french_w))
        else:
            dfs(sss[1:], english_w | sss[0], french_w)
            dfs(sss[1:], english_w, french_w | sss[0])

    dfs(ss, english_base, french_base)

    return res[0]


def format(out):
    return out

def solve(*args, **kwargs):
    return format(_solve(*args, **kwargs))

print(solve(("he loves to eat baguettes", "il aime manger des baguettes")), 1)
print(solve(("a b c d e", "f g h i j", "a b c i j", "f g h d e")), 4)
print(solve(("he drove into a cul de sac", "elle a conduit sa voiture", "il a conduit dans un cul de sac", "il mange pendant que il conduit sa voiture")), 3)
#sys.exit(0)

os.system('cp /home/mama/Downloads/%s.in .'%name)
os.system('rm /home/mama/Downloads/%s*.in'%name)
lines = open('%s.in'%name).readlines()
output = open('%s.out'%name, 'w')
cases = int(lines[0])
curline = 1
for caseno in range(cases):
    N = int(lines[curline].strip())
    curline += 1
    inp = []
    for _ in range(N):
        inp.append(lines[curline].strip())
        curline += 1
    inp = tuple(inp)
    res = str(solve(inp))
    #print(inp, caseno, res)
    print(caseno, '---')
    output.write('Case #%d: %s\n'%((caseno+1), res))
    output.flush()
output.close()
    








