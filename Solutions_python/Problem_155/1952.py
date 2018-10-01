import sys
import collections

def solve(s):
	d = 0
	a = s[0]
	for i, j in enumerate(s[1:]):
		if j:
			d += max(i+1 - (a+d), 0)
		a += j
	return d


if __name__ == '__main__':
	sys.stdin.readline()
	T = 0
	for line in sys.stdin:
		T += 1
		Smax, s = line.split()
		print "Case #{}: {}".format(T, solve(map(int, s)))

