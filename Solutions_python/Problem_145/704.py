import sys
import math

def possible(p, q):
	if p>q:
		p = p-q
	if p == 1:
		if q % 2 == 0:
			return True
	while q>p:
		if q % 2 != 0:
			return False
		q = q / 2.0
	return possible(p, q)

def solve(n, p,q):
	if q % 2 != 0:
		return "impossible"
	
	while q>p:
		n+=1
		q = q/2.0
		if q == 1:
			return n
		if q % 2 != 0:
			return "impossible"
	if possible(p, q):
		return n
	return "impossible"

T = int(sys.stdin.readline().strip())
for t in range(T):
	#print "Problem", t+1
	p, q = [int(v) for v in sys.stdin.readline().strip().split("/")]
	
	res = solve(0, p,q)	
	
	print "Case #{0}: {1}".format(t+1, res)

