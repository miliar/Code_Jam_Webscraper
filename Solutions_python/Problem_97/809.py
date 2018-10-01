#!/usr/bin/python
# -*- coding: utf-8 -*-

def line2intlist(line):
	list = line.split(' ')
	numbers = [ int(x) for x in list ]
	return numbers

def binomialCoefficient(n, k):
    if k < 0 or k > n:
        return 0
    if k > n - k: # take advantage of symmetry
        k = n - k
    c = 1
    for i in range(k):
        c = c * (n - (k - (i+1)))
        c = c // (i+1)
    return c

def rot(A, num):
	A = str(A)
	for i in xrange(0, num):
		A = A[-1] + A[0:-1]
	return int(A)

def getRotList(num, A, B):
	""" Only return bigger rotated ones """
	rotList = [num]
	for i in xrange(1, len(str(A))):
		tmp = rot(num, i)
		if (A <= tmp) and (tmp <= B) and (tmp not in rotList):
			rotList.append(tmp)
	return rotList
 
def recycled(A, B):
	pairs = 0
	lists = []
	for num in xrange(A, B+1):
		if num not in lists:
			tmpList = getRotList(num, A, B)
			if len(tmpList) > 1:
				pairs += binomialCoefficient(len(tmpList), 2)
				lists += tmpList
	return pairs
 
if __name__ == "__main__":
	testcases = input()
 
	for caseNr in xrange(0, testcases):
		A, B = line2intlist(raw_input())
		print("Case #%i: %i" % (caseNr+1, recycled(A, B)))
