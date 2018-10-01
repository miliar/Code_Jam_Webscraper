#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import izip
def check(ls): return all(p <= n for p,n in izip(ls, ls[1:]))

with open('small.in','r') as f: lines = f.read().splitlines()
cn = 1
for line in lines[1:]:
    stak = [line]
    while stak:
        x = stak.pop()
        if check(map(int,list(x)))==True: print 'Case #{}: {}'.format(cn,x)
        else: stak.append(str(int(x)-1))
    cn += 1