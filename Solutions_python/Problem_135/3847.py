#!/usr/bin/python2

import sys

infile = sys.stdin

T = int(infile.readline())
for x in range(1, T+1):
    c1 = []
    c2 = []
    s = []
    
    s.append(int(infile.readline().strip()))
    for _ in range(4):
        r = infile.readline().split()
        c1.append(r)

    s.append(int(infile.readline().strip()))
    for _ in range(4):
        r = infile.readline().split()
        c2.append(r)
    
    found = 0
    for r, card in enumerate(c1[s[0]-1]):
        if card in c2[s[1]-1]:
            fcard = card
            found += 1
    
    if found == 1:
        print("Case #%d: %s" %(x, fcard))
    elif found == 0:
        print("Case #%d: %s" %(x, "Volunteer cheated!"))
    else:
        print("Case #%d: %s" %(x, "Bad magician!"))

