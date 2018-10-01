#! /usr/bin/python

import sys
import math

def exec_test(Smax, Si):
	add = 0
	sumi = 0

	for n in xrange(Smax+1):
		if n==0:
			sumi += Si[0]
			continue
		
		if sumi<n:
			to_add = n-sumi
			add += to_add
			sumi += to_add

		sumi += Si[n]		

	return " %u" % add

# ====== READ INPUT ====================================

assert len(sys.argv)>=2, "Need input file"
input_file = sys.argv[1]
fd = open(input_file, 'r')
fd_out = open(input_file+".out", 'w')
n = int(fd.readline().split()[0]) # Number of tests
for test in xrange(n):
	print "=== Test #%i ===" % (test+1)
	nums = fd.readline().split()
	Smax = int(nums[0])
	Si = map(lambda x: int(x), nums[1])
	assert len(Si)==Smax+1, "Error length"
	ret = exec_test(Smax, Si)
	strret = "Case #%i:%s" % ((test+1), str(ret))
	print strret
	fd_out.write(strret+"\n")

