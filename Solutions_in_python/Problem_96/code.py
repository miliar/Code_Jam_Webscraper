from __future__ import division
import sys

infile = sys.stdin
t = int(infile.readline())
for j in xrange(t):
	l = list(map(int, infile.readline().split()))
	n=l[0]
	s=l[1]
	p=l[2]
	l=l[3:]
	triplet=[]
	for each in l:
		tick=0
		triplet.append(int(each/3))
	triplet=sorted(triplet,reverse=True)
	l=sorted(l,reverse=True)
	for i in xrange(len(triplet)):
		if triplet[i] >= p:
			tick+=1
		elif triplet[i]*3 <= l[i]:
			diff=l[i]-triplet[i]*3
			if diff==1 and p-triplet[i]==1 : 
				tick+=1
			elif diff==2 and (p-triplet[i]==2 )  and s>0 :
				tick+=1
				s-=1
			elif diff==2 and (p-triplet[i]==1 ):
				tick+=1
			elif diff==0 and p-triplet[i]==1 and s>0 and triplet[i]>0:
				tick+=1
				s-=1		
	print("Case #%d: %s" % (j+1, tick))		
