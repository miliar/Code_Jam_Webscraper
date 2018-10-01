import fileinput
from operator import mul

def gcd(a, b):
	while b != 0:
		a,b = (b,a%b)

	return a

def answer(X):
	d = [ x2 - x1 for x2,x1 in zip(X[1:], X[:-1]) ]

	prod = reduce(mul, d)
	div = reduce(gcd, d, prod)

	if X[0]%div == 0:
		return 0

	return div - X[0]%div

dat = [ [int(x) for x in line.split()] for line in fileinput.input() ]

for cn,d in enumerate(dat[1:]):
	print "Case #%d: %d" % ( cn+1, answer(sorted(d[1:])) )
