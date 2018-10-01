#!/usr/bin/env python

NPASS = 5000

def inp():
	return [eval(x) for x in raw_input().strip().split()]


class Chick:
	def __init__(self, b, t, l, v):
		self.l = l
		self.v = v
		self.t = (b - l + 0.0)/v
		if self.t > t:
			self.p = NPASS
		else:
			self.p = 0
	
	def __repr__(self):
		s = '(l%d, v%d, t%f, p%d)' % (self.l, self.v, self.t, self.p)
		return s


def solve(n, k, b, t):
	ll = inp()
	lv = inp()
	chl = []
	for l, v in zip(ll, lv):
		chl.append(Chick(b, t, l, v))
	
	chl.reverse()
	#print chl
	pswap = []
	for i in range(len(chl)):
		if chl[i].p == NPASS:
			continue
		#print chl[i], 'passed ',
		for j in range(i):
			if chl[j].p == NPASS:
				chl[i].p += 1
				#print chl[j],
		pswap.append(chl[i].p)
		#print chl[i].p, 'chickens'
	if len(pswap) < k:
		return 'IMPOSSIBLE'

	pswap.sort()
	cswap = sum(pswap[:k])
	#print cswap
	return cswap


def solveCase():
	n, k, b, t = inp()
	#print
	#print n, k, b, t
	cswap = solve(n, k, b, t)
	return cswap if cswap == 'IMPOSSIBLE' else "%d" % cswap
	return "%d, %d" % (n,k)

def main():
	[ncase] = inp()
	for i in xrange(ncase):
		print "Case #%d: %s" % (i+1, solveCase())

if __name__ == "__main__":
	main()

