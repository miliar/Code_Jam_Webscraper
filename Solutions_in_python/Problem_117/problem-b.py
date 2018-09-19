#!/usr/bin/python

import sys
import itertools

def higher_number_in_cross(lawn, h, w, x, y, value):
	row_found=False
	column_found=False
	for xx in xrange(h):
		if lawn[xx][y] > value:
			row_found=True
	for yy in xrange(w):
		if lawn[x][yy] > value:
			column_found=True
	return row_found and column_found

def is_pattern_possible(lawn, h, w):
	for x in xrange(h):
		for y in xrange(w):
			if higher_number_in_cross(lawn, h, w, x, y, lawn[x][y]):
				return False
	return True

def main():
    n_cases = int(sys.stdin.readline())
    for i in xrange(1,n_cases+1):
		lawn=[]
		h,w=map(int,sys.stdin.readline().strip().split(' '))
		for hh in xrange(h):
			lawn.append(sys.stdin.readline().strip().split(' '))
		if is_pattern_possible(lawn, h, w):
			print 'Case #{0}: YES'.format(i)
		else:
			print 'Case #{0}: NO'.format(i)
			

if __name__ == '__main__':
    main()
