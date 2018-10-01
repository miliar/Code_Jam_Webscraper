import sys
from math import *
from copy import copy, deepcopy
from itertools import product, permutations, combinations
from Queue import Queue


sys.setrecursionlimit(1500)


for test in range(1, int(raw_input()) + 1):

    n ,R, O, Y, G, B, V = map(int, raw_input().split())

    incre = sorted([R, Y, B])[::-1]
    ch = {}
    used = set()
    # who's R
    if incre[0] == R:
        ch['R'] = 'R'
        used.add('R')
    elif incre[0] == Y:
        ch['R'] = 'Y'
        used.add('Y')
    elif incre[0] == B:
        ch['R'] = 'B'
        used.add('B')

    # who's Y
    if incre[1] == R and 'R' not in used:
        ch['Y'] = 'R'
        used.add('R')
    elif incre[1] == Y and 'Y' not in used:
        used.add('Y')
        ch['Y'] = 'Y'
    elif incre[1] == B and 'B' not in used:
        used.add('B')
        ch['Y'] = 'B'

    #who's B
    for c in 'RBY':
        if c not in used:
            ch['B'] = c
    #print ch
    _R, _Y, _B = R, Y, B
    R, Y, B = incre
    #print R, Y, B

    _m = n / 2

    if max(max(R, Y), B) > _m:
        answer = 'IMPOSSIBLE'
    else:
        answer = ""
        last = None
        for _ in range(n):
            _m = sorted([R, Y, B])
            new_last = None
            if _m[2] == R and last != ch['R']:
                new_last = ch['R']
                R -= 1
            elif _m[2] == Y and last != ch['Y']:
                new_last = ch['Y']
                Y -= 1
            elif _m[2] == B and last != ch['B']:
                new_last = ch['B']
                B -= 1

            if new_last is None:
                if _m[1] == R and last != ch['R']:
                    new_last = ch['R']
                    R -= 1
                elif _m[1] == Y and last != ch['Y']:
                    new_last = ch['Y']
                    Y -= 1
                elif _m[1] == B and last != ch['B']:
                    new_last = ch['B']
                    B -= 1

            if new_last is None:
                if _m[0] == R and last != ch['R']:
                    new_last = ch['R']
                    R -= 1
                elif _m[0] == Y and last != ch['Y']:
                    new_last = ch['Y']
                    Y -= 1
                elif _m[0] == B and last != ch['B']:
                    new_last = ch['B']
                    B -= 1

            answer += new_last
            last = new_last



    print 'Case #{}: {}'.format(test, answer)

