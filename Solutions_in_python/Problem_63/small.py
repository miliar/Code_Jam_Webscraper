"""
Google Code Jam
    Round 1C 2010
        B
"""

from math import log,ceil

name="B-large"

def gotans(x,y):
	if log(x,y)<=1:
		return 0
	else:
		return gotans(y**(ceil(log(x,y)/2)),y)+1

with open(name+'.in','r') as infile:
    cases = int(infile.readline())
    with open(name+'.out','w') as outfile:
        for i in range(1,cases+1):
            # parse input
            L,P,C=tuple(map(int,infile.readline().split(' ')))
            # coding here:
            ans=gotans(ceil(P/L),C)
            # output the answers
            print('Case #',i,': ',ans,sep='',file=outfile)

