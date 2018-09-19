#!/usr/bin/pyhon

import sys
import re

""" usage: python task_a.py input_file_name

Requires python 2.x
"""

f = open(sys.argv[1])
line = f.readline()
(L, D, N) = [int(s) for s in line.split(' ')]
words = []
for i in range(D):
    words.append(f.readline())
for i in range(N):
    test = f.readline()
    test = test.replace('(', '[')
    test = test.replace(')', ']')
    p = re.compile(test)
    result = 0
    for w in words:
        if p.match(w):
            result += 1
    print "Case #%d: %d" % ((i + 1), result)
