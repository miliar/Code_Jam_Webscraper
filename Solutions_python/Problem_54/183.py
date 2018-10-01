# GCJ 2010 Qual 
# 2. Fair Warning

# May 8, 2010
# wookayin

import sys

def gcd(x, y):
	if y == 0: return x
	return gcd(y, x%y)

def solve(n, a):
	g = -1
	for x in a: 
		for y in a:
			if x != y:
				if g < 0: g = abs(x-y)
				else: g = gcd(g, abs(x-y))
	
	ans = g - a[0] % g
	if ans == g: return 0
	return ans

def main():
	infile = file("B-large.in", "r") 
	outfile = file("B-large.out", "w")
	T = int(infile.readline())

	for tt in xrange(1, T+1):
		a = map(int, infile.readline().split())
		n, a = a[0], a[1:]
		outfile.write("Case #%d: %d\n" % (tt, solve(n, a)))

if __name__ == "__main__":
	main()
