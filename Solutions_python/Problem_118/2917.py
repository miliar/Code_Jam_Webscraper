#!/usr/bin/python
from math import sqrt
def isP(n):
	if len(str(n)) == 1:
		return True
	else:
			return str(n)[::-1] == str(n)
def isS(n):
	ans = 0
	if n >= 0:
		if n == 1:
			return True
		if n >=0:
			while ans*ans < n:
				ans = ans+1	
			if ans*ans == n:
				return True
			else:
				return False
	else:
		return False
def isS2(n):
	n = n **.5
	return int(n) == n	
if __name__=="__main__":
	testcases = input()
	for case in range(testcases):
		start,end = raw_input().split(" ")
		out = 0
		for num in range(int(start),int(end)+1):
			if isP(num) and isS2(num) and isP(int(num**.5)):	
				out=out+1
		print "Case #%d: %d" % (case+1,out)
