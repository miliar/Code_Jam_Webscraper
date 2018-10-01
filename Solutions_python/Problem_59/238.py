#!/usr/bin/python

import sys, re, string, math

def do_one_case(cnum):
	(N,M) = map(int,sys.stdin.readline().split())
	root = {}
	c = 0
	
	for i in range(N+M):
		ee = sys.stdin.readline()[:-1].split("/")[1:]
		node = root
		
		for e in ee:
			if not node.has_key(e):
				node[e] = {}
				if i >= N:
					c += 1
			node = node[e]
	print "Case #%d: %d" % (cnum, c)

def main():
	T = int(sys.stdin.readline().strip())
	for i in range(T):
		do_one_case(i+1)


if __name__ == "__main__":
	main()
