
import sys, os
import math as m

if len(sys.argv)>1:
  fi=open(sys.argv[1])
else:
  fi=sys.stdin

ncases=int(fi.readline())

for case in xrange(ncases):
	P,K,L=map(int,fi.readline().strip('\n').split())
	ltrs=map(int,fi.readline().strip('\n').split())
	
	if (P*K)<L:
		print "Case #%i: Impossible"%(case+1)
	else:
		kp=0
		ltrs.sort(reverse=True)
		#print P,K,L,ltrs
		for i in xrange(P):
			for l in ltrs[K*i:K*(i+1)]:
				kp+=l*(i+1)
		
		print "Case #%i:"%(case+1),kp
	
