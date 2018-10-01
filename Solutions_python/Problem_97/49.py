# Tested and running on: 
# Python 2.7.2 (default, Jan 20 2012, 15:37:52) 
# [GCC 4.2.1 Compatible Apple Clang 3.0 (tags/Apple/clang-211.12)] on darwin

# (C) 2012 Dennis Bliefernicht

def process():
	(a,b) = map(lambda x: int(x), pop().split(" "))
	r = range(a, b+1)
	cnt = 0
	skiplist = []
	
	for n in r:
		s = str(n)
		seen = []
		for l in range(1,len(s)):
			# move l digits to the front and check
			s2 = s[len(s)-l:] + s[0:len(s)-l]
			n2 = int(s2)

			if n2 < n or n2 in seen:
				continue
				
			if (n2 != n) and (n2 >= a) and (n2 <= b):
				cnt += 1
				seen.append(n2)
		
	out(cnt)

# ------------------------------------
# GCJ2012 framework stuff
# ------------------------------------
import sys
import os

case_number = 1
lines = []

def out(*vals):
	global case_number
	print "Case #%d:" % case_number,
	for v in vals:
		print str(v),
	print
	case_number += 1
		
def output(fmt, *vals):
	global case_number
	print ("Case #%d: " + fmt) % ((case_number,) + vals)
	case_number += 1

def pop():
	global lines
	e = lines[0]
	lines = lines[1:]
	return e
	
def popint():
	return int(pop())
	
def popflt():
	return float(pop())
	
def main():
	global lines
	case_count = int(pop())
	for x in range(case_count):
		process()
	if len(lines) != 0:
		print "ERROR: %d lines remaining" % (len(lines))

if __name__ == "__main__":
	f = open(sys.argv[1])
	lines = map(lambda x: x[:-1], f.readlines())
	f.close()
	main()