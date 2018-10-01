#!/usr/bin/env python
# -*- coding: utf8 -*-
# Johan Musaeus Bruun, 20090903

import sys
from numpy import *

sys.setrecursionlimit(5500)

MAX = 10000
currentcolor = 0

def main(fin):
	global currentcolor
	debug = False
	alphabet = "_abcdefghijklmnopqrstuvwxyz"
	
	T = int(fin.readline()) # T = number of maps/cases
	
	for case in xrange(T):
		H, W = map(int, fin.readline().split()) # height (rows) and width (columns)
		z = fromfile(fin, sep=' ', count=H*W, dtype=int16).reshape(H,W) # input matrix
		m = zeros(H*W,dtype=int16).reshape(H,W) # output matrix
		
		print "Case #%d:" % (case+1)
		
		#print z # temp
		
		for x in xrange(H):
			for y in xrange(W):
				m[x,y] = childcolor(z,m,x,y,debug)
		
		for x in xrange(H):
			s = ""
			for y in xrange(W):
				s = s + alphabet[m[x,y]] + " "
			print s[:-1]
		
		currentcolor = 0

################################


def childcolor(z,m,x,y,debug):
	global currentcolor
	if debug: print "Considering (%d,%d)" % (x, y)
	if m[x,y] != 0:
		if debug: print "- color %d found at (%d,%d)" % (m[x,y],x,y)
		return m[x,y]
	bx, by, ba = x, y, val(z,x,y) # best altitude
	if val(z,x-1,y) < ba:
		bx, by, ba = x-1, y, val(z,x-1,y)
	if val(z,x,y-1) < ba:
		bx, by, ba = x, y-1, val(z,x,y-1)
	if val(z,x,y+1) < ba:
		bx, by, ba = x, y+1, val(z,x,y+1)
	if val(z,x+1,y) < ba:
		bx, by, ba = x+1, y, val(z,x+1,y)
	if debug: print "- best step is (%d,%d) with altitude %d" % (bx, by, ba)
	if bx==x and by==y: # we're at a sink without color
		currentcolor = currentcolor + 1
		newcolor = currentcolor
		m[x,y] = newcolor
		return newcolor
	else:
		m[x,y] = childcolor(z,m,bx,by,debug) 
		return m[x,y]


def val(matrix,row,col):
	if row<0 or col<0 or row>=matrix.shape[0] or col>=matrix.shape[1]:
		return MAX
	return matrix[row,col]


################################

if __name__ == '__main__':
	try:
		#inputfile = "B-test2.in"
		#fin = open(inputfile, 'r')
		fin = sys.stdin 
		main(fin)
	except IOError:
		print "File I/O error!"
