#!/usr/bin/python
import os
import sys

def gcd(a,b):
	if a < b:
		return gcd(b,a)
	else:
		if b == 0:
			return a
		return gcd(b,a%b)

def solve( nums ):
	pass

sys.stdin = open("warning.in","r");
sys.stdout = open("warning.out","w");

#print "solved it: ",solve( [1,10,11] )

T = int( raw_input() )

#print "Got ", T, " tests"

for i in range(T):
	line = raw_input().split()
	num =  int( line[0] )

	nums = []
	for j in range(1,num+1):
		nums.append( int( line[j] ) )
	
	nums.sort()

	#print "Test case#%d" % (i+1)
	#print nums

	diff = []
	for j in range( len(nums)-1 ):
		diff.append( nums[j+1]-nums[j] )
	#print "Difference table"
	
	diff = [ di for di in diff if di ]

	if len(diff) == 0:## no such thing... it's infinity
		print "inifinity"
		continue

	maxT = reduce( gcd , diff )
	#print "Maximum T is", maxT
	
	count = len( nums )

	for j in range( len(nums) ):
		if nums[j] % maxT == 0:
			count-=1
		else:
			break

	if not count:
		print "Case #%d: 0" % (i+1);## already divided by that number
	else:
		print "Case #%d: %d" % (i+1,(maxT-nums[0]%maxT))
