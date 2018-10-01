#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys
from math import *

def sqr(x): return x*x


def inte3(x):
    return x*sqrt(1-sqr(x))/2 + asin(x)/2

def inte2(rad, low):
    return inte3(low/rad) * sqr(rad)

def inte(rad, low, high):
    # int(sqrt(rad^2-x^2), x=low..high)
    return inte2(rad, high) - inte2(rad, low)


def solve(f, R, t, r, g):
    if 2 * f > g: return 1.0

    i = 0

    racket_rad = R - t - f
    sum_area = 0.0

    while True:
	# for this 
	ylower = (r+f) + (2*r + g) * i
	yupper = (r+g-f) + (2*r + g) * i

	if sqr(racket_rad) - sqr(ylower) < r: break
	if sqr(racket_rad) - sqr(yupper) < r:
	    xlimit = -1
	else:
	    xlimit = sqrt(sqr(racket_rad) - sqr(yupper))

	# (r+g-f) + (2*r+g) * j <= xlimit

	perfect_j = floor( (xlimit - (r+g-f)) / (2*r+g) )
	if perfect_j < -1: perfect_j = -1

	sum_area += (perfect_j+1.0) * sqr(g-2*f)
	j = perfect_j+1.0

	while True:
	    xlower = (r+f) + (2*r + g) * j
	    xupper = (r+g-f) + (2*r + g) * j

	    if (sqr(xlower) + sqr(ylower) >= sqr(racket_rad)): break

	    D0 = (sqr(xlower) + sqr(ylower) <= sqr(racket_rad))
	    D1 = (sqr(xupper) + sqr(ylower) <= sqr(racket_rad))
	    D2 = (sqr(xlower) + sqr(yupper) <= sqr(racket_rad))
	    D3 = (sqr(xupper) + sqr(yupper) <= sqr(racket_rad))

	    tarea = 0.0


	    if not D1 and not D2:
		ymed = sqrt(sqr(racket_rad) - sqr(xlower))
		tarea = inte(racket_rad, ylower, ymed) - xlower*(ymed - ylower)
		#   int(y = ylower..ymed, sqrt(racket_rad^2 - y^2) - xlower
	    elif D1 and not D2:
		#   int(x = xlower..xupper, sqrt(racket_rad^2 - x^2) - ylower
		tarea = inte(racket_rad, xlower, xupper) - ylower * (xupper - xlower)

	    elif not D1 and D2:
		#   int(y = ylower..yupper, sqrt(racket_rad^2 - y^2) - xlower
		tarea = inte(racket_rad, ylower, yupper) - xlower * (yupper - ylower)

	    else:
		#   (xmed-xlower)*(g-2*f)  + int(x=xmed..xupper, sqrt(racket_rad^2-x^2) - ylower)
		xmed = sqrt(sqr(racket_rad) - sqr(yupper))
		tarea = (xmed-xlower)*(g-2*f) + inte(racket_rad, xmed, xupper) - ylower* (xupper - xmed)
    
	    #print "IJ: ", i, j, tarea

	    sum_area += tarea
	    j += 1.0

	#print "PERFECT: ", perfect_j + 1.0

	i += 1


    return 1.0 - sum_area / (pi * sqr(R) / 4)

if __name__ == "__main__":
    if len(sys.argv) >= 2:
	inf = file(sys.argv[1], 'r')
    else:
	inf = sys.stdin

    of = sys.stdout

    T = int(inf.readline())

    for t in xrange(1, T+1):
	of.write("Case #%d: " % t)

	f, R, t, r, g = map(float, inf.readline().strip().split())
	soln = 0.0

	of.write("%f\n" % solve(f, R, t, r, g));
	

 

