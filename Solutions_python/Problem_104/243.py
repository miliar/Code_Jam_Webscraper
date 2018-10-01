# coding: utf8

import os, sys, re, string
import math,random

def calc(values):
	cache = {values[0]: [str(values[0])]}
	for v in values[1:]:
		s = [str(v)]
		for k in cache.keys():
			newv = k + v
			if cache.has_key(newv):
				return [' '.join(cache[newv]), ' '.join(cache[k] + s)]
			cache[newv] = cache[k] + s
	return False

def main():
	T = int(sys.stdin.readline().strip())
	for i in xrange(T):
		values = map(int, sys.stdin.readline().split(' '))
		results = calc(values[1:])
		print "Case #%d:" % (i + 1)
		if results:
			print "\n".join(results)
		else:
			print "Impossible"

if __name__ == '__main__':
	main()


