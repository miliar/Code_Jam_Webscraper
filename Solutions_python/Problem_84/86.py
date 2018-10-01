#!/usr/bin/env python
import sys
import math

current = sys.argv[1].split('.')[0]

f = open('%s.in' % current, 'r')
g = open('%s.out' % current, 'w')
lines = f.readlines()
f.close()

def red(inp):
    for i in range(len(inp)):
        for j in range(len(inp[i])):
            if inp[i][j] == '#':
                try:
                    if inp[i][j+1] == '#' and inp[i+1][j] == '#' and inp[i+1][j+1] == '#':
                        inp[i][j] = '/'
                        inp[i][j+1] = '\\'
                        inp[i+1][j] = '\\'
                        inp[i+1][j+1] = '/'
                    else:
                        return 'Impossible'
                except IndexError:
                    return 'Impossible'
    return '\n'.join(''.join(i) for i in inp)

case = int(lines[0])
cur = 1
for i in range(1, case + 1):
    r, c = [int(x) for x in lines[cur].split()]
    inp = []
    for j in range(1, r+1):
        inp.append(list(lines[cur+j][:c]))
    cur += 1 + r
    #print 'Case #%d:\n%s' % (i, red(inp))
    g.write('Case #%d:\n%s\n' % (i, red(inp)))

g.close()
