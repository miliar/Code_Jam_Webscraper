#!/usr/bin/python

import re

def input1():
	n_cases=int(raw_input())
	for i in range(n_cases):
		s=raw_input()
		s=re.split(' ',s)
		P=int(s[0])
		K=int(s[1])
		L=int(s[2])
		if P*K<L:
			print "Case #%d: impossible" % (i+1)
		s=raw_input()
		s=re.split(' ',s)
		freq=[]
		for j in range(len(s)):
			freq.append(int(s[j]))
		freq.sort(reverse=True)
		count=0
		c=1
		m=0
		keys=[]
		for j in range(1,len(freq)+1):
			count+=freq[j-1]*c
			if j%K==0:
				c+=1
				


		print "Case #%d: %d" % (i+1,count)


input1()
