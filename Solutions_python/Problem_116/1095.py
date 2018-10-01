#!/usr/bin/env python2
# coding: utf-8

from itertools import islice
import sys

T = int(sys.stdin.readline())

val = { '.' : 0, 'X' : 1, 'O' : 2, 'T' : 3 }
msk = { 1426063360 : 'X won',
        5570560 : 'X won',
        21760 : 'X won',
        85 : 'X won',
        1077952576 : 'X won',
        269488144 : 'X won',
        67372036 : 'X won',
        16843009 : 'X won',
        1074791425 : 'X won',
        17043520 : 'X won',
        2852126720 : 'O won',
        11141120 : 'O won',
        43520 : 'O won',
        170 : 'O won',
        2155905152 : 'O won',
        538976288 : 'O won',
        134744072 : 'O won',
        33686018 : 'O won',
        2149582850 : 'O won',
        34087040 : 'O won' }


for case in range(1,T+1):
    field = 0
    filled = True
    for line in islice(sys.stdin, 5):
        for char in line.rstrip():
            field = (field * 4) + val[char]
            if char == '.':
                filled = False

    for k, v in msk.items():
        if (field & k) == k:
            ans = v
            break
    else:
        ans = 'Draw' if filled else 'Game has not completed'

    print 'Case #%d: %s' % (case, ans)
