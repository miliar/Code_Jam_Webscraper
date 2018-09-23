import numpy as np
import random as rx
import math
import os



f = open('input.txt', 'r')
numcases = int(f.readline().rstrip('\n'))

for i in range(1,numcases+1):

    if( i == 16):
        qq = 1

    x = f.readline().rstrip('\n')
    xb = x.split()

    N = int(xb[0])
    R = int(xb[1])
    O = int(xb[2])
    Y = int(xb[3])
    G = int(xb[4])
    B = int(xb[5])
    V = int(xb[6])
    mem = np.zeros((3,1))

    strx = ""
    last = "X"
    lose = 0
    while(N > 0):
        next = ""
        N = N-1
        if (last == "X"):
            if (B >= Y and B >= R):
                last = "B"
                strx = strx+last
                B = B-1
                heavy = "B"
                l1 = "Y"
                l2 = "R"
                mem[0] = B
                mem[1] = Y
                mem[2] = R
            elif(Y>=R):
                last = "Y"
                strx= strx+last
                Y = Y-1
                heavy = "Y"
                l1 = "B"
                l2 = "R"
                mem[0] = Y
                mem[1] = B
                mem[2] = R
            else:
                last = "R"
                strx= strx+last
                R = R-1
                heavy = "R"
                l1 = "B"
                l2 = "Y"
                mem[0] = R
                mem[1] = B
                mem[2] = Y
        elif (heavy == last):
            if mem[1] >= mem[2]:
                last = l1
                strx = strx+last
                mem[1] = mem[1] - 1
            else:
                last = l2
                strx = strx+last
                mem[2] = mem[2] - 1
        elif last == l1:
            if mem[0] >= mem[2]:
                last = heavy
                strx = strx+last
                mem[0] = mem[0] - 1
            else:
                last = l2
                strx = strx+last
                mem[2] = mem[2] - 1
        else:  #last == l2:
            if mem[0] >= mem[1]:
                last = heavy
                strx = strx+last
                mem[0] = mem[0] - 1
            else:
                last = l1
                strx = strx+last
                mem[1] = mem[1] - 1


    if (mem[0] < 0 or mem[1] < 0 or strx[0] == strx[-1]):
        print "Case #" + str(i) +": "+"IMPOSSIBLE"
    else:
        print "Case #" + str(i) +": "+strx