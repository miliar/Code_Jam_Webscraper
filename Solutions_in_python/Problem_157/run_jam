#! /usr/bin/python

import sys
import math

lkup = { 	(1,1)       : (1,1),
					(1,'i')     : (1,'i'),
					(1,'j')     : (1,'j'),
					(1,'k')     : (1,'k'),
					('i',1)     : (1,'i'),
					('i','i')   : (-1,1),
					('i','j')   : (1,'k'),
					('i','k')   : (-1,'j'),
					('j',1)     : (1,'j'),
					('j','i')   : (-1,'k'),
					('j','j')   : (-1,1),
					('j','k')   : (1,'i'),
					('k',1)     : (1,'k'),
					('k','i')   : (1,'j'),
					('k','j')   : (-1,'i'),
					('k','k')   : (-1,1)		}

def prod(a_s, b_s):
	s = a_s[0] * b_s[0]
	(s2, l) = lkup[( a_s[1], b_s[1] )]
	return (s*s2, l)

def power(a_s, n):
	if a_s[1]==1:
		return (a_s[0]**n, 1)
	else:
		if n%4==0:
			res = (1,1)
		elif n%4==1:
			res = (1,a_s[1])
		elif n%4==2:
			res = (-1,1)
		else:
			res = (-1,a_s[1])
		return (res[0]*(a_s[0]**n), res[1])

def exec_test(L, X, string):

	#Check that product is -1
	pi = (1,1)
	for s in string:
		pi = prod(pi, (1,s))
	pi = power(pi, X)

	if pi!=(-1,1):
		return " NO"

	#Find first "i"
	pi = (1,1)
	done=[]
	found=0
	pnum=0

	while pnum<=X-1:

		if pi in done:
			break
		done.append(pi)

		for i_s in xrange(len(string)):
			s = string[i_s]
			pi = prod(pi, (1,s))
			if pi==(1,'i'):
				found=1
				found_i=i_s+L*pnum
				break

		if found==1:
			break

		pnum+=1		
	
	if found==0:
		return " NO"	

	#Find first "k" reverse
	pi = (1,1)
	done=[]
	found=0
	pnum=0

	while pnum<=X-1:

		if pi in done:
			break
		done.append(pi)

		for i_s in reversed(xrange(len(string))):
			s = string[i_s]
			pi = prod((1,s), pi)
			if pi==(1,'k'):
				found=1
				found_k=i_s+L*(X-1-pnum)
				break

		if found==1:
			break

		pnum+=1		
	
	if found==0:
		return " NO"	

	#IF here means we found both i from left and k from right
	# mathematically q is in between

	if found_k>found_i:
		return " YES"

	return " NO"

# ====== READ INPUT ====================================

assert len(sys.argv)>=2, "Need input file"
input_file = sys.argv[1]
fd = open(input_file, 'r')
fd_out = open(input_file+".out", 'w')
n = int(fd.readline().split()[0]) # Number of tests
for test in xrange(n):
	print "=== Test #%i ===" % (test+1)
	nums = fd.readline().split()
	(L, X) = (int(nums[0]), int(nums[1]))
	string = fd.readline()[:-1]
	assert len(string)==L, "Error length"
	ret = exec_test(L, X, string)
	strret = "Case #%i:%s" % ((test+1), str(ret))
	print strret
	fd_out.write(strret+"\n")

