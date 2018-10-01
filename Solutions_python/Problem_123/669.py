# -*- coding: utf-8 -*-
T=int(raw_input())

def solve(motes,start,end,cur):
	if end-start<1:
		return 0
	nex=motes[start]
	if cur>nex:
		return solve(motes,start+1,end,cur+nex)
	else:
		mote=solve(motes,start+1,end,cur);
		if cur!=1:
			m=solve(motes,start,end,2*cur-1)
		else:
			return 1+mote
		return 1+min(mote,m)

for _iter in xrange(T):
	count=0
	A,N=map(int,raw_input().split())
	motes=map(int,raw_input().split())
	motes.sort()
	print "Case #%d: %d" % (_iter+1,solve(motes,0,N,A))