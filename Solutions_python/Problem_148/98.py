# -*- coding: utf-8 -*-
# Google Code Jam
# Create Date: 2014-04-10
# Created by: buaamm
#--------------------------------------------------------------------
import sys
import os

def nextint():
	return (int)(fr.readline())

def nextints():
	return map(int, next().strip().split())
	
def next():
	return fr.readline()

def write(s):
	fw.write(str(s))
	
def writeline(s):
	fw.write(str(s) + "\n")

def repeat(s, r):
	for i in range(r):
		fw.write(s)

def reprep(s, len, r):
	for i in range(r):
		repeat(s, len)
		write("\n")

def draw_single(n,m):
	write("c")
	repeat("*", m-1)
	write("\n")
	reprep("*", m, n-1)
def draw_line(a,b):
	repeat(".", a)
	repeat("*", b)
	write("\n")



#--------------------------------------------------------------------
def solve():
	n,m = nextints()
	sizes = nextints()
	#print sizes
	tbl = [ 0 for i in range(m+1) ]
	for i in range(n):
		tbl[sizes[i]] += 1
	remain = n
	ans = 0
	while remain > 0:
		if remain == 1:
			ans += 1
			break
		ans += 1
		sz1 = -1
		for i in range(m):
			sz = m-i
			if tbl[sz] > 0:
				tbl[sz] -= 1
				sz1 = sz
				break
		assert sz1 >= 0
		for i in range(m-sz1, 0, -1):
			if tbl[i] > 0:
				tbl[i] -= 1
				remain -= 1
				break
		remain -= 1
	write("%d\n" % ans)
	#	Solve
	
	#write("%d\n" % dp[39][0][0])
	
#--------------------------------------------------------------------
if __name__ == "__main__": ##__name__: [filename].py
	print "Hello, Main."
else:
	global fr, fw
	prob_name = "A-large"

	fr = open(prob_name + '.in', 'r')
	fw = open(prob_name + '.out', 'w')
	cas = (int)(fr.readline())
	for cs in range(cas):
		write("Case #%d: " % (cs+1) )
		solve()
	fr.close()
	fw.close()
#--------------------------------------------------------------------


