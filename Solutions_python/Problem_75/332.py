#!/usr/bin/env python
import sys

current = sys.argv[1].split('.')[0]

f = open('%s.in' % current, 'r')
g = open('%s.out' % current, 'w')
lines = f.readlines()
f.close()

def final(l):
    cc = int(l.pop(0))
    c = {}
    lc, l = l[:cc], l[cc:]
    for i in lc:
        c[''.join(sorted(i[:2]))] = i[2:]
    dc = int(l.pop(0))
    d = []
    ld, l = l[:dc], l[dc:]
    for i in ld:
        d.append(''.join(sorted(i)))
    n = int(l.pop(0))
    l = list(l[0][:n])
    nl, l = [l[0]], l[1:]
    for i in l:
        nl.append(i)
        lt = ''.join(sorted(nl[-2:]))
        if lt in c:
            nl, lt = nl[:-2], c[lt]
            nl.append(lt)
        else:
            for j in d:
                if set(j).issubset(nl):
                    nl = []
    return ', '.join(nl)

case = int(lines[0])
for i in range(1, case + 1):
    l = lines[i].split(' ')
    #print 'Case #%d: [%s]' % (i, final(l))
    g.write('Case #%d: [%s]\n' % (i, final(l)))

g.close()
