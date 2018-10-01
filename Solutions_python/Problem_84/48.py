#!/usr/bin/python -OO

import sys;
import math;

def readia():
	return [int(x) for x in sys.stdin.readline().strip().split()];
def readsa():
	return sys.stdin.readline().strip().split();
def readi():
	return int(sys.stdin.readline().strip());
def reads():
	return sys.stdin.readline().strip();
def perr(s):
	print >>sys.stderr, s;

def tryCover(matr, x, y):
	if matr[x][y] == '#' and matr[x][y+1] == '#' and matr[x+1][y] == '#' and matr[x+1][y+1] == '#':
		matr[x][y] = '/';
		matr[x][y+1] = '\\';
		matr[x+1][y] = '\\';
		matr[x+1][y+1] = '/';


def main():
	T = readi();
	for t in xrange(T):
		(numRows, numCols) = readia();
		matr = [];
		for i in xrange(numRows):
			matr.append(list(reads()));
		res = True;
		if numRows >= 2 and numCols >= 2:
			for x in xrange(numRows - 1):
				for y in xrange(numCols - 1):
					tryCover(matr, x, y);

		for row in matr:
			for c in row:
				if c == '#':
					res = False;
					break;

		print "Case #%d:" % (t+1);
		if res:
			print "\n".join("".join(row) for row in matr);
		else:
			print "Impossible";

			
main();
