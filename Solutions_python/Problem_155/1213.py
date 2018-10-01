#coding: utf-8
#! /usr/bin/env python2.7

import sys

def main():
	line = []
	for l in sys.stdin:
		line.append(l[:-1])

	c = 0
	T = int(line[c])

	c += 1
	for i in range(T):
		smax, s_strings = line[c].split()
		ans = 0
		total = 0
		for j,k in enumerate(s_strings):
#			print j,k,total,ans
			if total < j:
				ans += j-total
				total += j-total
			total += int(k) 
		print "Case #%d: %d" % (i+1, ans)
		c += 1

if __name__ == "__main__":
	main()
