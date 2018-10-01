#!/usr/bin/python

import sys

p=[]


def check(n,m,t):
	for ni in xrange(n):
		for mi in xrange(m):
			r=True
			for ri in xrange(n):
				if t[ri][mi]>t[ni][mi]:
					r=False						
			c=True
			for ci in xrange(m):
				if t[ni][ci]>t[ni][mi]:
					c=False
			if not r and not c:
				return "NO"
	return "YES"
								

lines=sys.stdin.readlines()

x=1
case=1
while x<len(lines):
	n,m=map(int,lines[x].split())
	t=map(lambda x : map(int,x.split()), lines[x+1:x+n+1])
	print "Case #%d: %s" % (case,check(n,m,t))
	case+=1	
	x+=n+1	
	
