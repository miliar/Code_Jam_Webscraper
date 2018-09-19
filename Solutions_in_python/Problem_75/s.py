#!/usr/bin/env python
import sys

debug = False
def diff(a,b):
    if a < b: return b - a
    return a - b

line = []
#for l in open('sample', 'r'):
for l in sys.stdin:
    l = l.rstrip('\n')
    line.append(l)

T = int(line[0])

for i in range(T):
    l = line[i + 1].split(' ')

    C = int(l.pop(0))
    CList = []
    if C > 0:
        for j in range(C):
            a = l.pop(0)
            b = [k for k in a]
            CList.append(b[:3])
            b = b[3:]

    D = int(l.pop(0))
    DList = []
    if D > 0:
        for j in range(D):
            a = l.pop(0)
            b = [k for k in a]
            DList.append(b[:2])
            b = b[2:]

    N = int(l.pop(0))
    a = l.pop(0)
    NList = [k for k in a]

    E = []

    if debug:
        print "C:", CList
        print "D:", DList
    for j in range(N):
        E.append(NList[j])
        if debug:
            print ">", E

        # conbine
        for c in CList:
            l = len(E) - 1
            if l <= 0: continue
            if (E[l - 1] == c[0] and E[l] == c[1]) or (E[l - 1] == c[1] and E[l] == c[0]):
                DoProc = True
                if debug:
                    print 'conbine'
                    print E
                E.pop()
                E.pop()
                E.append(c[2])
                if debug:
                    print E
        # opporsed
        for d in DList:
            try:
                E.index(d[0])
                E.index(d[1])
                E = []
            except:
                continue

    if len(E) == 0:
        ans = "[]"
    else:
        ans = ""
        a = E.pop(0)
        ans = "[%s" % a
        while len(E) > 0:
            a = E.pop(0)
            ans += ", %s" % a
        ans += "]"

    print 'Case #%d: %s' % (i + 1, ans)
    del l
