#!/usr/bin/python
import sys, re

lines = open(sys.argv[1]).readlines()
L=int(lines[0].split()[0])
D=int(lines[0].split()[1])
N=int(lines[0].split()[2])

case = 0
for line in lines[1+D:]:
	r = 0
	case += 1
	for word in lines[:1+D]:
		m=re.match(line.replace('(', '[').replace(')', ']'), word)	
		if m != None: r += 1
	print "Case #%d: %d" % (case, r) 
