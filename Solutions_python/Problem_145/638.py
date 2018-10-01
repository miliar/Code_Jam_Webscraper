from math import *
from fractions import gcd
import sqlite3,time
import psutil, os

#set high priority
p = psutil.Process(os.getpid())
p.set_nice(psutil.HIGH_PRIORITY_CLASS)


def log2(a):
	a = log(a)
	a /= log(2)
	return a

t = int(raw_input())
for q in xrange(t):
	a,b = [int(i) for i in raw_input().split("/")]
	print "Case #%s:"%(q+1),
	if a < b:
		n = gcd(a,b)
		a /= n
		b /= n
		if log2(b) != int(log2(b)):
			print "impossible"
		else:
			ans = int(log2(b))
			if a == 1:
				print ans
			else:
				for i in range(0,ans):
					if a > b/2:
						break
					b /= 2
				print i+1
