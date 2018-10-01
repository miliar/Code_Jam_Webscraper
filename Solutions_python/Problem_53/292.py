#!/usr/bin/env python
#-*- coding: UTF-8 -*-

import sys

argv = sys.argv[1:]

fin = open(argv[0])
count = int(fin.readline().strip())


def solve(n, k):
    states = [False] * n
    for claps in range(k):
        for index, state in enumerate(states):
            states[index] = not state
            if not state:
                break
    return all(states) 
        

for index in range(count):
    n, k = [int(item) for item in fin.readline().strip().split()]
    solution = solve(n, k)
    print "Case #%d: %s" % (index+1, "ON" if solution else "OFF")