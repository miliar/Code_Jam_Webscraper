#!/usr/bin/env python

# Google code jam 2012

import sys

def nosurprise_max(tot):
    if tot % 3 == 0:
        return tot//3
    else:
        return tot//3+1

# s : surprises
# p : threshold
def result(n,s,p,l):
    base_count = 0
    pot_surprise = []

    pot_change = 0
    for e in l:
        r = nosurprise_max(e)
        if r >= p:
            base_count += 1
        elif e >= 2 and e % 3 != 1 and r == p - 1:
            pot_change += 1

    return str(base_count+min(pot_change,s))



    
p = int(sys.stdin.readline())
for q in range(1,p+1):
    l = []
    line = sys.stdin.readline()

    n,_,line = line.partition(' ')
    n = int(n)
    s,_,line = line.partition(' ')
    s = int(s)
    p,_,line = line.partition(' ')
    p = int(p)
    for i in range(n):
        val,_,line = line.partition(' ')
        l.append(int(val))

    print("Case #" + str(q) + ": " +  result(n, s,p, l))

