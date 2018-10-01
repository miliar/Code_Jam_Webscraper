#!/usr/bin/env python
from sys import stdout

#fin = open("data/C-small-attempt0.in", 'r')
fin = open("data/C-large.in", 'r')
#fout = stdout
fout = open("data/c.out", 'w')

def rotate(s, n):
    return s[-n:]+s[:-n]

cases = int(fin.readline())
#cases = 1
for ci in xrange(cases):
    a, b = map(int, fin.readline().split())
    #a, b = 1, 2000000
    result = 0
    for i in xrange(a, b):
        si = str(i)
        l = len(si)
        used = []
        for j in xrange(l):
            m = rotate(si, j)
            if m[0] != '0':
                m = int(m)
                if m <= b and m > i and m not in used:
                    #print si, " ", m
                    used.append(m)
                    result += 1


    fout.write("Case #%d: %s\n" % (ci+1, result))

