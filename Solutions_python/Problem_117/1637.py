#!/usr/bin/env python

import sys
import string

fname=sys.argv[1]

i=open(fname,'r')
o=open(fname+'.out','w')

'''readline Split'''
def rls(i):
	out=map(int, string.split(i.readline()))
	return out[0] if len(out)==1 else out

'''Output Case#...'''
def wout(o, i, arg):
	out="Case #"+ str(i)+":"
	out+=" "+str(arg)
	#out+=" "+''.join(arg)
	#for arg in args:
	#    out+=" "+str(arg)
	out+="\n"
	o.write(out)

T=rls(i)

for x in range(T):
	N,M=rls(i)
	out=[rls(i) for j in range(N)]
	print 
	for j in range(N):
		print "-", out[j]

	if N==1 or M==1:
		wout(o, x+1, 'YES')
		continue
	nMin=[min(out[n]) for n in range(N)]
	print nMin
	outTran=zip(*out)
	#print outTran
	mMin=[min(outTran[m]) for m in range(M)]
	print mMin
	gotoNext=False
	for n in range(N):
		for m in range(M):
			min_n = min(out[n])
			sum_n = sum(out[n])
			if out[n][m]==min_n and sum_n != min_n*M:
				min_m=min(outTran[m])
				sum_m = sum(outTran[m])
				if out[n][m]==min_m and sum_m != min_m*N:
					print n, m, M, min_n, sum_n, N, min_m, sum_m
					wout(o, x+1, 'NO')
					gotoNext=True
					break
		if gotoNext:
			break
	else:
		wout(o, x+1, 'YES')

