import sys
import re
from Numeric import *
from random import random

# ---------------------------------------------------------------------------------------------------------------

sys.setcheckinterval(10000)
PI = arccos(-1)
PI_2 = arccos(-1) / 2

# ---------------------------------------------------------------------------------------------------------------
# Global variables
#src_table = array(zeros(256), Int)

# ---------------------------------------------------------------------------------------------------------------


# USAR R-t no R !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def ig(x, r):
	if x == r: return 0
	return 0.5 * (arctan(x / sqrt(r**2 - x**2)) * r**2 + x * sqrt(r**2 - x**2))

def area(xd,xh,yd, r):
	return ig(xh, r) - ig(xd, r) - yd*(xh-xd)

def h(x, r):
	return sqrt(r**2-x**2)

def hLessThan(y, r):
	return sqrt(r**2-y**2)


def solve(caseNum):
	fs = 0.0000000000001
	f, R, t, r, g = 	map(float, sys.stdin.readline().strip().split(" "))
	if 2.0*f >= g:
		sys.stdout.write("Case #%d: %.6f" % (caseNum, 1))
		return

	rin = R - t - f
	g = g-2*f
	r = r + f
	sx = r
	sy = r
	if g <= 0 or rin <=0:
		sys.stdout.write("Case #%d: %.6f" % (caseNum, 1))
		return

	nohit = 0.0
	while(sx < rin):
		while(sy < h(sx, rin)):
			techo = min(rin, sy + g)
			piso = sy
			l = min(sx, rin)
			rig = min(sx + g, rin)
			if h(l,rin) <= techo:
				x = l
			else:
				x = hLessThan(techo, rin)

			if h(rig,rin) < piso:
				rig = hLessThan(piso, rin)

			myH = techo - piso
			if(x  < l):
				a = area(x, rig, piso,rin)
				nohit += a
			else:
				if(x > rig):
					nohit += (rig-l) * myH
				else:
					nohit += (x-l) * myH
					nohit += area(x,rig,piso,rin)
			sy += g + 2 * r
		sy = r
		sx += g + 2 * r

	nohit = nohit * 4
	phit = 1 - nohit / (R**2 * PI)

	sys.stdout.write("Case #%d: %.6f" % (caseNum, phit))


# ---------------------------------------------------------------------------------------------------------------
casesCount = int(re.findall(r'[\d]+', sys.stdin.readline())[0])
first = True
for case in range(1, casesCount + 1):
	if(first):
		first = False
	else:
		print ""
	solve(case)
