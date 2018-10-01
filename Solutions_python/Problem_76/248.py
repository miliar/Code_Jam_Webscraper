#!/usr/bin/python

fp = open('C-large.in')

fp.readline()

def solve(res):
	s = 0
	res.sort()
	res = res[1:]
	for i in res:
		s = s + i
	return s

c = 0

for line in fp:
	if c % 2 == 1:
		arr = [int(x) for x in line[:-1].split(' ')]
		res = 0
		for item in arr:
			res = res ^ item
		if res != 0:
			print "Case #%d: NO" % (c/2+1)
		else:
			print "Case #%d: %d" % ((c/2+1), solve(arr))
	c = c + 1
