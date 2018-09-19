#!/usr/bin/python
import sys
from math import log, ceil
with open('A-sm.in','r') as f:
    inputs= f.readlines()

inputs = [line.strip() for line in inputs]

with open('A-sm.out', 'w') as f:
    cases = int(inputs.pop(0))
    for test in range(cases):
        s = inputs.pop(0)
          
        r, c, w = s.split(' ')

        r = int(r)
        c = int(c)
        w = int(w)
        possible_positions = c - w + 1
        blanks = c - w
        ships =  w
        pos = [0 for i in range(c)]
        result = int(ceil(float(c)/w) + w - 1)
        #result = int(ceil(log(c - w + 2) / log(2)) + w -1)
        f.write('Case #' + str(test + 1) + ': ' + str(result) + '\n')

