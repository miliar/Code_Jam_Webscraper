#!/usr/bin/python
# -*- coding: utf-8 -*-

from pprint import pprint as _p

with open('A-large.in') as f:
    with open('2015_a.out', 'w') as fo:
        lines = f.readlines()
        t = int(lines[0].strip())
        for i in range(1, t + 1):
            max_shyness, xa = lines[i].strip().split()
            c = 0
            s = 0
            for j, ppl in enumerate(xa):
                if s + c < j:
                    c += 1
                s += int(ppl)
            fo.write('Case #%s: %s\n' % (i, c))