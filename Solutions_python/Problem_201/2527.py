#!/usr/bin/python3.6

from itertools import count
from functools import partial
from math import ceil


def next_line_to_ints(lines):
    return map(int, next(lines).split(' '))


f_in = open('c.in')
f_out = open('c.out', 'w')

lines = (i for i in f_in.read().splitlines())
t = int(next(lines))
fprint = partial(print, file=f_out)
# fprint = partial(print)

for case, line in enumerate(lines):
    stalls, persons = [int(n) for n in line.split(' ')]
    spaces = [0, stalls, 0]
    for _ in range(persons):
        # print(spaces)
        best = max(spaces)
        i = spaces.index(best)
        # print(best, i)
        best -= 1
        # print(best)
        rs = best//2
        ls = ceil(best/2)
        # print(ls)
        # print(ls, rs)
        spaces[i] = ls
        spaces.insert(i + 1, rs)

    fprint(f'Case #{case + 1}: ', ls, rs)
