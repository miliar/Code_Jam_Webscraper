#!/usr/bin/python
def rl(f,fn=lambda x:x):
	return fn(f.readline().strip())
import sys
f=open(sys.argv[1])
tc=rl(f,int)
for i in range(0,tc):
	vals=map(int,rl(f,lambda x:x.split(" ")))
	ng,s,p = vals[0:3]
	scores = vals[3:]
	possible=0
	for score in scores:
		mod = score % 3
		q = score/3
		# print "Modulus=%d, q=%d, score=%d" % (mod,q,score)
		if p > score:
			continue
		if q >= p:
			possible = possible + 1
		elif mod == 0 and (q+1) >= p and s>0:
			possible = possible + 1
			s=s-1
		elif (mod == 1 or mod == 2) and (q+1) >= p:
			possible = possible + 1
		elif mod == 2 and (q+2) >= p and s > 0:
			possible = possible + 1
			s=s-1
	print "Case #%d: %d" % (i+1,possible)