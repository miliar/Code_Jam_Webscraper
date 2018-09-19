from sys import stdin
import sys

fin = stdin

T = int(fin.readline())

EPS = 1e-8

def same(a,b):
	return (a+EPS>b and b+EPS>a)

for tc in xrange(T):
	(n,v,x) = map(float, fin.readline().split(' '))
	n = int(n)
	r = [0.0, 0.0]
	c = [0.0, 0.0]
	for i in xrange(n):
		(r[i],c[i]) = map(float, fin.readline().split(' '))
	pos = True
	ans = 0.0
	a1 = 0.0
	a2 = 0.0
	if n == 1:
		if same( c[0], x ):
			pos = True
			ans = v / r[0]
			a1 = ans
			a2 = 0
		else:
			pos = False
	if n == 2:
		if same( c[0], c[1] ):
			if same( c[0], x ):
				pos = True
				ans = v / (r[0]+r[1])
				a1 = a2 = ans
			else:
				pos = False
		
		else:
			t = (v * (x-c[1])) / (r[0] * (c[0]-c[1]))
			t2 = (v-r[0]*t)/r[1]
			if t*r[0] > v+EPS or t2*r[1] > v+EPS:
				pos = False
			else:
				pos = True
				ans = max( t, t2 )
				a1 = t
				a2 = t2
	#if pos:
	#	print "%.10f %.10f" % (a1, a2)
	#else:
	#	print "-1 -1"
	if pos:
		print "Case #%d: %.10f" % (tc+1, ans)
	else:
		print "Case #%d: IMPOSSIBLE" % (tc+1)