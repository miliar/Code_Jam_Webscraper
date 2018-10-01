#!/usr/bin/env python
#-*- coding: utf-8 -*-

import itertools
from math import sqrt

def is_palin(w):
    i = 0
    for c in reversed(w):
        if c != w[i]:
            return False
        i += 1
    return True

def gen_palin(s):
    if s < 10:
        for p in range(1,10):
            if p >= s:
                yield p

    k=len(str(s))
    if k < 2: k += 1
    while 1:
        #God Bless StackOverflow!
        for p in (sum([n*(10**i)\
            for i,n in enumerate(([x]+list(ys)+[z]+list(ys)[::-1]+[x])\
            if k%2 else ([x]+list(ys)+list(ys)[::-1]+[x]))])\
            for x in range(1,10)\
            for ys in itertools.permutations(range(10), k/2-1)
            for z in (range(10) if k%2 else (None,))):

            if p >= s:
                yield p
        k += 1

for t in xrange(int(raw_input())):
    answer = 0
    a, b = [int(x) for x in raw_input().split()]
    g = gen_palin(int(round(sqrt(a))))

    square = g.next()**2

    while square <= b:
        if square >= a:
            if is_palin(str(square)):
                answer += 1
        square = g.next()**2

    print 'Case #' + str(t+1) + ': ' + str(answer)
