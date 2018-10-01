# https://code.google.com/codejam/contest/3274486/dashboard

import math, itertools
def solve(n, k, array):
	choices = itertools.combinations(array, k)
	res = []
	for choice in choices:
		tmp = 0
		largest = 0
		for r, h in choice:
			tmp += 2 * r * h * math.pi
			largest = max(largest, r)
		res.append(tmp +  math.pi * largest * largest)
	return "{0:.7f}".format(max(res))

if __name__ == '__main__':
	t = int(raw_input())
	for i in range(1,t+1):
		n, k = map(int, raw_input().split())
		array = []
		for j in range(n):
			tmp = map(int, raw_input().split())
			array.append(tmp)
		print "Case #{}:".format(i), solve(n, k, array)







