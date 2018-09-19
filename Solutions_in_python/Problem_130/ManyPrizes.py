import sys, math
sys.setrecursionlimit(10001)

def to_int(sol):
	return int(sol.replace("W", "0").replace("L", "1"), 2)

def best_case(idx, below):
	if below == 0:
		return "L" * (N - idx)
	return "W" + best_case(idx + 1, int(math.ceil(below / 2.0) - 1))

def worst_case(idx, above):
	if above == 0:
		return "W" * (N - idx)
	return "L" + worst_case(idx + 1, int(math.ceil(above / 2.0) - 1))

def best_bin_search():
	x = 0
	y = 2 ** N - 1
	while x < y:
		mid = x + (y - x + 1) / 2
		could = best_case(0, 2 ** N - mid - 1)
		couldI = to_int(could)
		if couldI + 1 <= P:
			x = mid
		else:
			y = mid - 1
	return x

def worst_bin_search():
	x = 0
	y = 2 ** N - 1
	while x < y:
		mid = x + (y - x + 1) / 2
		could = worst_case(0, mid)
		couldI = to_int(could)
		if couldI + 1 <= P:
			x = mid
		else:
			y = mid - 1
	return x

T = int(sys.stdin.readline().strip())
for t in xrange(1, T+1):
	N, P = map(int, sys.stdin.readline().strip().split())
	print "Case #{}: {} {}".format(t, worst_bin_search(), best_bin_search())
