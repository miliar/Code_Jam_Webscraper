from sys import stdin
import operator

def solve():
	n, = map(int, stdin.readline().split())
	a = map(int, stdin.readline().split())

	if reduce(operator.xor, a) != 0:
		return False

	return sum(a) - min(a)

n, = map(int,stdin.readline().split())
for i in range(n):
	print "Case #{}: {}".format(i+1, solve() or "NO")
