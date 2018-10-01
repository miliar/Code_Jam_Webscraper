#!/usr/bin/python
# Thomas Karpiniec

num_cases = int(raw_input())

for case in xrange(num_cases):
	n = int(raw_input())
	v1 = []
	v2 = []
	v1s = []
	v2s = []
	v1s = raw_input().split()
	v2s = raw_input().split()
	for i in v1s:
		v1.append(int(i))
	for j in v2s:
		v2.append(int(j))
	
	v1.sort()
	v2.sort()
	v2.reverse()
	
	#m = n - 1
	#for i in xrange(n - 1):
	#	if v2[i] == 0:
	#		v2.pop(i)
	#		v2.append(0)
	#		m -= 1
	#	if i == m:
	#		break
	
	
	#print v1
	#print v2
	
	sum = 0
	for a,b in zip(v1, v2):
		sum += a*b
	
	print "Case #%d: %d" % (case+1, sum)
	