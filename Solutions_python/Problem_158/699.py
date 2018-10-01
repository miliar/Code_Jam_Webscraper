#!/usr/bin/python
import sys
import math

ifile=sys.argv[1]
lines=open(ifile).read().split("\n")
lines=lines[1:]
case=1

debug=False
#debug=True



def processCase(x, r, c):
    winner="RICHARD"
    if (r * c) % x == 0:
        winner="GABRIEL"
    highD=int(math.ceil(x/2.0))
    if highD > r or highD > c:
        winner="RICHARD"
    if x > c and x > r:
        winner="RICHARD"
    if x == 4 and ((c == 2) or (r == 2)):
        winner="RICHARD"
    return winner
    


for line in lines:
    if line == '':
        break
    [x,r,c]=line.split(' ')
    output=processCase(int(x), int(r), int(c))
    if debug:
        print("input: "+ line + " Case #"+str(case)+": "+str(output))
    else:
        print("Case #"+str(case)+": "+str(output))
    case+=1
	
	
