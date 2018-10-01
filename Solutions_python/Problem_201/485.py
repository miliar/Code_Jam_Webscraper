#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
import sys
import math

def insert(dico, width, slots):
    if width not in dico:
        dico[width] = slots
    else:
        dico[width] += slots
    return dico

with open(sys.argv[1], 'r') as f:
    for n in range(int(f.readline())):
        N, K = [int(i) for i in f.readline().split()]
        spaces = {N:1}
        while K > 0:
            width = max(spaces.keys())
            slots = spaces.pop(width)
            if width %2 == 1:
                y = width/2
                z = width/2
                spaces = insert(spaces, width/2, 2*slots)
            else:
                spaces = insert(spaces, width/2, slots)
                spaces = insert(spaces, width-width/2-1, slots)
                y = width/2
                z = width-width/2-1
            K -= slots
        print("Case #"+str(n+1)+": "+str(y)+' '+str(z))
        
