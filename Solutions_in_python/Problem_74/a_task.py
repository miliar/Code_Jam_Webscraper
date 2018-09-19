#! /usr/bin/python -tt

import sys

def readarray(f):
    return [x for x in f.readline().split(" ")]

f = open(sys.argv[1], 'r')
t = int(readarray(f)[0])
for i in range(1, t+1):
    data = readarray(f)
    n = int(data[0])
    o, b = 1, 1
    ox, bx = 0, 0
    st = 0
    for it in xrange(n):
        name, s = data[2*it+1], int(data[2*it+2])
        if name == 'B':
            bx_ = abs(b - s)
            if ox > 0:
                st += ox
                if bx_ <= ox:
                    bx_ = 0
                else:
                    bx_ = bx_ - ox
                ox = 0
            bx += bx_ + 1
            b = s
        elif name == 'O':
            ox_ = abs(o - s)
            if bx > 0:
                st += bx
                if ox_ <= bx:
                    ox_ = 0
                else:
                    ox_ = ox_ - bx
                bx = 0
            ox += ox_ + 1
            o = s
#        print name, s, "bx=", bx, "ox=", ox, st
    if ox > 0: st += ox
    if bx > 0: st += bx
    print "Case #%d: %s" % (i, st)


