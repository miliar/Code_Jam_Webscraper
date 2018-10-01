# Run in command line
# E:\python27\python_nopause.bat C.py < "C-test.in" > "C-test-out.txt" 2>&1
# E:\python27\python_nopause.bat C.py < "C-small-1-attempt0.in" > "C-small-1-out.txt" 2>&1
# E:\python27\python_nopause.bat C.py < "C-large.in" > "C-large-out.txt" 2>&1

import os
from sys import *
from math import *

def emptystall(n, k, num):
	# print 'n,k,num =', n, k, num		
	if n == 1:
		return [0,0]
	else:
		Ls = int(floor((n-1)/2.))
		Rs = int(ceil((n-1)/2.))		
		if k == 1:
			return [Ls,Rs]
		else:
			num = num+[Ls, Rs]
			k-=1
			n-=1
			np = max(num)	
			num.remove(max(num))
			return emptystall(np,k,num)
			

T = int(stdin.readline())
for t in xrange(T):
	N, K = map(int,stdin.readline().split())
	# print N, K
	num = []
	res = emptystall(N,K,num)
	print  "Case #%s:" %(t+1), max(res), min(res)