#!/usr/bin/env python

import string

ipt = open("q3l.i", "r")
opt = open("q3l.o", "w+")

cases = int(ipt.readline())
#print cases

for case in range(cases) :
	candies = int(ipt.readline())
#	print candies
	candylist = ipt.readline().rsplit(" ")
#	print candylist
	a = 0

	for i in range(candies) :
		candylist[i] = int(candylist[i])
		a ^= int(candylist[i])
#		print a

	if a != 0 :
		print "Case #%d: NO" % (case+1)
		opt.write("Case #%d: NO\n" % (case+1))
		continue

	candylist.sort()
#	print candylist
	a = 0
	b = 0
	for i in range(candies-1) :
		a += int(candylist[i+1])
		b = b ^ int(candylist[i+1])
#	print candylist
#	print b
	print( "Case #%d: %d" % (case+1, a))

	opt.write("Case #%d: %d\n" % (case+1, a))

ipt.close()
opt.close()




