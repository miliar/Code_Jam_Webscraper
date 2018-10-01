# -*- coding: utf-8 -*-
from __future__ import with_statement

import sys


class Item():
    def __init__(self, R, P):
        self.R = R
        self.P = int(P)

def move(tp, cp):
    if tp is None:
        return cp

    if tp.P-cp>0:
        cp+=1
    elif tp.P-cp<0:
        cp-=1
    return cp

argvs = sys.argv
argc = len(argvs)

infile = argvs[1]
outfile = "out"

if argc < 2:
    print "error"


with open(infile, "r") as f:
    lines = f.read().splitlines()
    
T = int(lines[0])

outlines=[]
for i in range(1, T+1):
    ss = lines[i].split(" ")
    N = int(ss[0])
    B = []
    O = []
    step = []
    for j in range(1, N*2+1, 2):
        item = Item(ss[j], ss[j+1])
        if item.R == "O":
            O.append(item)
        else:
            B.append(item)
        step.append(item.R)

    stepnum = 0
    bp=op=1
    o=b=None

    if len(O)>0:
        o = O.pop(0)
    if len(B)>0:
        b = B.pop(0)
    if len(step)>0:
        action = step.pop(0)
   
    while 1:
        #print " %3d: action=%s, bp=%d, b.P=%d, op=%d, o.P=%d\n" % (stepnum, action, bp, b.P, op, o.P)

        stepnum+=1
        if (b!=None and action=="B" and bp==b.P) \
            or (o!=None and action=="O" and op==o.P):
            if len(step)==0:
                break

            if action=="B":
                if len(B)>0:
                    b=B.pop(0)
                else:
                    b=None
                op=move(o, op)
            elif action=="O":
                if len(O)>0:
                    o=O.pop(0)
                else:
                    o=None
                bp=move(b, bp)
            action = step.pop(0)

        else:
            bp=move(b, bp)
            op=move(o, op)

    outlines.append("Case #%d: %d" %(i, stepnum))


with open(outfile, "w") as f:
    for line in outlines:
        f.write(line + "\n")


