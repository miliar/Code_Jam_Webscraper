#! /usr/bin/env python
#################################################################################
#     File Name           :     Problem A. Standing Ovation.py
#     Created By          :     xiaodi
#     Creation Date       :     [2015-04-12 07:19]
#     Last Modified       :     [2015-04-12 07:26]
#     Description         :      
#################################################################################


T = int(raw_input())
for t in xrange(T):
	
	raw = raw_input()
	tt = raw.split()
	Smax = int(tt[0])
	l = map(int, list(tt[1]))
	audience = dict()
	for x in xrange(len(l)):
		audience[x] = l[x]
	standing = audience[0]
	friends = 0
	for x in xrange(1, Smax+1):
		if standing >= x:
			standing = standing + l[x]
		else:
			more = x - standing
			friends = friends + more
			standing = standing + more + l[x]
		# print x, standing, friends, l[x]
	print "Case #%d:" % (t+1), friends





