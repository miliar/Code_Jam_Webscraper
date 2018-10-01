#!/usr/bin/python
import sys, re, string, math

def do_one_case(cnum):
	(L,P,C) = map(int, sys.stdin.readline().split())
	
	n = C
	tmp = 1
	while L * n < P:
		n *= C
		tmp += 1
	n = 1
	ans = 0
	while tmp > n:
		ans += 1
		n *= 2
	
	print "Case #%d: %d" % (cnum, ans)

def main():
	T = int(sys.stdin.readline().strip())
	for i in range(T):
		do_one_case(i+1)

if __name__ == "__main__":
	main()
