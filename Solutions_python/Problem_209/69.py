import math
import itertools

def main():
	n = int(input())
	for i in range(1, n+1):
		print("Case #%d: " % i, end="")
		solve()

def solve():
	n, k = map(int, input().split())
	cakes = [list(map(int, input().split())) for _ in range(n)]
	
	asds = []
	for i, b in enumerate(cakes):
		rest = cakes[:i] + cakes[i+1:]
		asd = math.pi*b[0]**2 + score(b)
		scores = map(score, filter(lambda x: x[0] <= b[0], rest))
		asd += sum(sorted(scores, key=lambda x: -x)[:(k-1)])
		asds.append(asd)
	print(max(asds))

def score(cake):
	return 2*math.pi*cake[0]*cake[1]

main()