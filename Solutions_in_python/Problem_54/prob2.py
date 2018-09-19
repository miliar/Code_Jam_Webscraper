#!/usr/bin/python
import math
import fractions

c = int(raw_input())
Case = 1
for i in range(0,c):
	s = (raw_input())	
	
	ar = s.split(' ')
	n = int(ar[0])
	del ar[0]
	#print ar
	#for j in range(0,n):
	#	p = int(raw_input())
	#	ar.append(p)
	diff = []

	for j in range(0,n-1):
		diff.append(int(ar[j+1])-int(ar[j]))

	if(len(diff)<2):
		GCD = diff[0]
	elif(len(diff)==2):	
		GCD = fractions.gcd(diff[0],diff[1])
	elif(len(diff)>2):
		GCD = fractions.gcd(diff[0],diff[1])
		for j in range(2,len(diff)):
			GCD = fractions.gcd(GCD,diff[j])
	
	if(GCD<0):
		GCD = GCD*(-1)
	
	d = int(ar[0])%GCD
	if d == 0:
		res = 0
	else:
		res = GCD - d
	print 'Case #%d: %d' %(Case,res)

	Case = Case +1
