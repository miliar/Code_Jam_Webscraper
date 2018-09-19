#!/usr/bin/python

import string

def convert(s):
	lc = string.lowercase
	lc = 'abcdefghijklmnopqrstuvwxyz'
	gg = 'ynficwlbkuomxsevzpdrjgthaq'
	trans = string.maketrans(gg,lc)
	return string.translate(s,trans)


f = open('A-small-attempt0.in')
ind = 1
count = int(f.readline())
for line in f:
	sout = convert(line)
#	print line
	print "Case #" + str(ind) + ": " + sout,
	ind = ind + 1


#if __name__ == "__main__":
#	input = sys.stdin
