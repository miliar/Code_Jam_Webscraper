import sys
from fractions import Fraction
li=[]
sys.setrecursionlimit(1500)
table=[]
n=0
d=0

def time_comp(pos):
	if pos>=n-1:
		table[n-1]=n_time_comp(n-1)
		return table[pos]
	if table[pos]==-1:
		table[pos]=max(n_time_comp(pos), time_comp(pos+1))
		return table[pos]
	else:
		return table[pos]

def n_time_comp(pos):
	return float(Fraction((d-li[pos][0]),li[pos][1]))

t=int(raw_input())

for t0 in xrange(t):
	d, n=map(int, raw_input().strip().split())
	li=[]

	table=[-1] * n
	for i in xrange(n):
		k0, s0=map(int, raw_input().strip().split())
		li.append((k0, s0))

	li=sorted(li)

	ti=time_comp(0)


	print "Case #%d: %f"%(t0+1, float(d/ti))