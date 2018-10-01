import sys
import math

file = sys.stdin

def ispalindrome(n):
	s = str(n)
	k = len(s)
	for i in range(0,k/2):
		if s[i] != s[k-1-i]:
			return 0
	return 1

def countfairandsquare(A,B):
	count = 0
	n = int(math.sqrt(A))
	bound = int(math.sqrt(B))
	while n*n < A:
		n += 1
	while n <= bound:
		if ispalindrome(n) and ispalindrome(n*n):
			count += 1
		n += 1
	return count

n = int(file.readline())

for k in range(1,n+1):
	line = file.readline()
	templst = [int(x) for x in line.split(" ")]
	assert(len(templst) == 2)
	A = templst[0]
	B = templst[1]
	res = countfairandsquare(A,B)
	print "Case #{0}: {1}".format(k,res)
