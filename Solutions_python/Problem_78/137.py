#!/usr/bin/python

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

def nod(a, b):
	while a % b > 0:
		c = a % b;
		a = b;
		b = c;
	return b;

def calcd(pd):
	if pd == 0:
		return 1;
	else:
		return 100 / nod(100, pd);

def main():
	T = readi();
	for t in xrange(0, T):
		(N, pd, pg) = readia();
		d = calcd(pd);
		res = True;
		if d > N:
			res = False;
		elif pd < 100 and pg == 100 or pd > 0 and pg == 0:
			res = False;
		print "Case #%d: %s" % (t + 1, "Possible" if res else "Broken");

		#nd = d * pd / 100;
		#z = nd * 100 - pg * d;
		#print d, nd, z, pg;
		#g = calcd

			
main();
