import sys

from math import *
from itertools import *
from collections import defaultdict

def lg(a) :
    sys.stderr.write(str(a)+"\n")

def prin(ones) :
    mx = max([ x for (x,y) in ones ])+1
    my = max([ y for (x,y) in ones ])+1
    for y in range(my) :
	for x in range(mx) :
	    if (x,y) in ones :
		print "1",
	    else :
		print " ",
	print

t = int(sys.stdin.readline())
for testNr in range(1,t+1) :
    r = int(sys.stdin.readline())
    rs = []
    ones = set()
    for i in range(r) :
	a = map(int,sys.stdin.readline().split())
	a[2] += 1
	a[3] += 1
	assert len(a)==4
	rs.append(a)
	for x in range(a[0],a[2]) :
	    for y in range(a[1],a[3]) :
		ones.add((x,y))
    rnd = 0
    while len(ones)>0 :
#	prin(ones)
#	print "----"
	nexts = set()
	for p in ones :
	    x = (p[0]-1,p[1])
	    y = (p[0],p[1]-1)
	    if x in ones or y in ones :
		nexts.add(p)
	for x in ones :
	    p = (x[0]+1,x[1])
	    y = (p[0],p[1]-1)
	    if y in ones :
		nexts.add(p)
	    
	ones = nexts
	rnd += 1
    print "Case #%d:" % testNr ,
    print rnd
