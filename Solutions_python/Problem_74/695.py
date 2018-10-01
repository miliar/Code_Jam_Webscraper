'''
Created on May 6, 2011

@author: dan
'''

def score(s):
    otime, btime, opos, bpos = 0,0,1,1
    a = s.split()
    num = int(a.pop(0))
    for i in range(num):
        player = a.pop(0)
        button = int(a.pop(0))
        if player == "O":
            otime = otime + abs(opos - button) + 1
            if otime <= btime:
                otime = btime + 1
            opos = button
        elif player == "B":
            btime = btime + abs(bpos - button) + 1
            if btime <= otime:
                btime = otime + 1
            bpos = button
    if otime > btime :
        return otime
    return btime

import sys
if (len(sys.argv) >1) :
    fname = sys.argv[1]
else:
    fname = "../input.txt"
f = open(fname)
for j in range(int(f.readline())):
    print "Case #"+str(j+1)+": "+str(score(f.readline()))