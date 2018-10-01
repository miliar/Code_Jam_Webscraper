import math
import sys

def gcd(a,b):
	while b > 0:
		a, b = b, a%b
	return a

def lcm(a, b):
	return a*b/gcd(a,b)

c = int(sys.stdin.readline())
for x in range(0, c):
	i = sys.stdin.readline().split()
	n = int(i[0])
	t = [0] * n
	min = 10e400
	for x1 in range(0, n):
		t[x1] = int(i[x1+1])
		if t[x1]<min:
			min=t[x1]
	diff = set()
	for x1 in range(0, n):
		for x2 in range(x1+1, n):
			diff.add(abs(t[x1]-t[x2]))
	d = -1
	for di in diff:
		if d == -1:
			d = di
		else:
			d = gcd(d, di)

	min = -min
	while min < 0:
		min += d
	
	print "Case #"+str(x+1)+":", min
