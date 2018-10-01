#!/usr/bin/env python
import sys

T = int(raw_input())
c_count=0
while T:
	googlers = map(lambda a: int(a), raw_input().split())
	#N = googlers[0]
	S = googlers[1]
	p = googlers[2]
	del(googlers[0]); del(googlers[0]);	del(googlers[0])
	
	hit=0
	ppp=3*p

	for g in googlers:
		if g >= ppp-2:
			hit+=1
		elif S and g in range(2,29): #just for sure
			if g >= (ppp-4):
				hit+=1
				S-=1
	
	c_count+=1
	print 'Case #{0}: {1}'.format(str(c_count), str(hit))

	T-=1
