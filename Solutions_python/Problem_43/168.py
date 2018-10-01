#!/usr/bin/env python
# -*- coding: utf8 -*-
# Johan Musaeus Bruun, 20090912

import sys

def main(fin):
	
	T = int(fin.readline()) # T = number of cases
	#print T, "cases..." # temp
	
	for case in xrange(T):
		x = trimn(fin.readline())
		#print "Bases in this case:", bases # temp
		
		base = getbase(x) 
		if base == 1:
			base = 2
		
		y = makey(x,base)
		
		out = int(y, base)
		
		print "Case #%d: %s" % (case+1, out)


################################

def makey(x,base):
	y = ""
	chars = "1023456789abcdefghijklmnopqrstuvwxyz"
	c = 0
	d = {}
	for v in x:
		if v not in d:
			new = chars[c]
			c = c + 1
			y = y + new
			d[v] = new
		else:
			# v is in d
			y = y + d[v]
	return y


def getbase(x):
	diff= 0
	for c in "0123456789abcdefghijklmnopqrstuvwxyz":
		if x.count(c) > 0:
			diff = diff + 1
	return diff


def trimn(s):
	#return (s[-1] == '\n') ? s[:-1] : s
	if len(s) > 1 and s[-1] == '\n':
		return s[:-1]
	else:
		return s


################################

if __name__ == '__main__':
	try:
		#inputfile = "A-test2.in"; fin = open(inputfile, 'r')
		fin = sys.stdin
		main(fin)
	except IOError:
		print "File I/O error!"
