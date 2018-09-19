'''
Created on 13.09.2009

@author: DorianG
Python 3
'''
import sys
from math import sqrt


inFile = open(sys.argv[1], 'r')
outFile = open('output', 'w')
for i in range(1, eval(inFile.readline()) + 1):
    flies = []
    nflie = eval(inFile.readline())
    for j in range(nflie):
        flies.append([eval(x) for x in inFile.readline().split()])
    center = [sum(x[i] for x in flies) for i in range(6)]
    #center = [x/nflie for x in center]
    print (center)
    s = center[0:3]
    v = center[3:6]
    t = 0 - sum(s[i] * v[i] for i in range(3))
    nv = sum(ve * ve for ve in v)
    if nv == 0:
        t = 0.0
        d = sqrt(sum(se * se for se in s)) / nflie
    elif t < 0:
        t = 0.0
        d = sqrt(sum(se * se for se in s)) / nflie
    else:
        t = t / nv
        dv = [s[i] + t * v[i] for i in range(3)]
        d = sqrt(sum(dve * dve for dve in dv)) / nflie
    outFile.write("Case #{}: {:.8f} {:.8f}\n".format(i, d, t))
    
inFile.close()
outFile.close()
