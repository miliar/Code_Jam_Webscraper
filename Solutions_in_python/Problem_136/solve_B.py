#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def cookie(t):
	C, F, X = map(float, t.split(" "))
	old = 0
	new = C/2
	nb_f = F
	while (old+X/(nb_f-F+2)) > (new+X/(nb_f+2)):
		old = new
		new += C/(nb_f+2)
		nb_f += F
	return old+X/(nb_f-F+2)

if __name__ == "__main__":
	with open(sys.argv[1]) as f:
		buf = f.read()
	t = buf.split("\n")
	nb_boards = int(t[0])
	t = t[1:]
	for k in xrange(0, nb_boards):
		print "Case #%d: %s"%(k+1, cookie(t[k]))
