# Tested and running on: 
# Python 2.7.2 (default, Jan 20 2012, 15:37:52) 
# [GCC 4.2.1 Compatible Apple Clang 3.0 (tags/Apple/clang-211.12)] on darwin

# (C) 2012 Dennis Bliefernicht

# obtained via analyzing the example text by hand
m = ['y', 'n', 'f', 'i', 'c', 'w', 'l', 'b', 'k', 'u', 'o', 'm', 'x', 's', 'e', 'v', 'z', 'p', 'd', 'r', 'j', 'g', 't', 'h', 'a', 'q']

def process():
	text = pop()
	result = ""
	
	for c in text:
		if c == ' ':
			result += ' '
		else:
			result += chr(ord('a') + m.index(c))

	out(result)

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