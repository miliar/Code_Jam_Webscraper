# -*- coding: utf-8 -*-
import sys
import math

f_in = sys.argv[1]
f_out = sys.argv[2]

testcases=[]

with open(f_in) as f:
    T = int(f.readline())
    for t in range(T):
	f.readline()
	testcases.append(f.readline())

for k,t in enumerate(testcases):
    t=[int(a) for a in t.strip().split(' ')]
    
    if max(t)<=3:
	ans=int(max(t))
    else:
	steps = []
	nmax = max(t)
	for i in range(1,int(nmax)+1):
	    moves = 0
	    for j in t:
		if j > i:
		    while j>i:
			j=j-i
			moves = moves +1
	    steps.append(moves+i)
#	print 'Case #'+str(k+1),t
#	print steps
	ans=int(min(steps))

    with open(f_out,'a') as g:
#	print '------>', str(ans)
	g.write('Case #'+str(k+1)+': '+str(ans)+'\n')
