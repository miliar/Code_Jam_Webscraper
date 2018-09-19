#!/usr/bin/python

from sys import argv
import fileinput

def get_top(s):

    min = max = None
    for i in xrange(3):
        if (s + i) % 3 == 0:
             z = (s + i) / 3
             if z <= 10: min = z
     
    for i in xrange(2, 5):
        if (s + i) % 3 == 0:
             z = (s + i) / 3
             if z <= 10 and z > 1: max = z

    return (min, max)

def solve(s, p, t):
        c = 0
        for i in t:
            (min, max) = get_top(i)
            #print min, max
            if min >= p:
                c += 1
            elif max is None or p > max:
                continue
            elif s > 0:
                c += 1
                s -= 1
        return c


i = 1
for line in fileinput.input():
    if fileinput.isfirstline():
        continue

    print "Case #" + str(i) + ":",
    i += 1
    f = line.split()
    s = int(f[1])
    p = int(f[2])
    t = [int(x) for x in f[3:]]
    print solve(s, p, t)

