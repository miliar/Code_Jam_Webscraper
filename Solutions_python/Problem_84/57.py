import sys

from math import *
from itertools import *
from collections import defaultdict

# http://code.activestate.com/recipes/123641-hopcroft-karp-bipartite-matching/
from matching import *

def lg(a) :
    sys.stderr.write(str(a)+"\n")

def f(r,c,m) :
    poses = []
    for i in range(r-1) :
	for j in range(c-1) :
	    poses.append((i+j,i,j))
    poses.sort()
    tiles = []
    for s,i,j in poses :
	if m[i][j]==0 :
	    continue
	if m[i][j]+m[i+1][j]+m[i][j+1]+m[i+1][j+1]==4 :
	    m[i][j]=0
	    m[i+1][j]=0
	    m[i][j+1]=0
	    m[i+1][j+1]=0
	    tiles.append((i,j))
	else :
	    print "Impossible"
	    return
    summ = sum([ m[i][j] for i in range(r) for j in range(c) ])
    if summ>0 :
	print "Impossible"
	return
    for i in range(r) :
	for j in range(c) :
	    m[i][j] = '.'
    for (i,j) in tiles :
	m[i][j] = '/'
	m[i+1][j] = '\\'
	m[i][j+1] = '\\'
	m[i+1][j+1] = '/'
#    print m
    for l in m :
	print "".join(l)

t = int(sys.stdin.readline())
for testNr in range(1,t+1) :
    r,c = map(int,sys.stdin.readline().split())
#    print r,c
    m = []
    st = []
    for i in range(r) :
	a = [ 1 if ch=="#" else 0 for ch in sys.stdin.readline().strip() ]
	m.append(a)
#    lg(m)
    print "Case #%d:" % testNr
    f(r,c,m)

