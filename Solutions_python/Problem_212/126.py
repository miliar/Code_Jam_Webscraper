from collections import defaultdict

getl = lambda: tuple(input().strip().split())
get = lambda: tuple(map(int, getl()))

def memo(f):
	cache = dict()
	def wrap(*args):
		if args not in cache: cache[args] = f(*args)
		return cache[args]
	return wrap


@memo
def solve3(r, r1, r2):
	if r1 == 0 and r2 == 0:
		return 0
	res = 0
	if r1 != 0:
		res = max(res, solve3((r + 1) % 3, r1 - 1, r2))
	if r2 != 0:
		res = max(res, solve3((r + 2) % 3, r1, r2 - 1))
	return (1 if r == 0 else 0) + res

@memo
def solve4(r, r1, r2, r3):
	if r1 == 0 and r2 == 0 and r3 == 0:
		return 0

	res = 0
	if r1 != 0:
		res = max(res, solve4((r + 1) % 4, r1 - 1, r2, r3))
	if r2 != 0:
		res = max(res, solve4((r + 2) % 4, r1, r2 - 1, r3))
	if r3 != 0:
		res = max(res, solve4((r + 3) % 4, r1, r2, r3 - 1))

	return (1 if r == 0 else 0) + res


def solve(N, P, G):
	g = defaultdict(lambda: 0)
	for x in G:
		g[x % P] += 1

	if P == 2:
		return g[0] + (g[1] + 1) // 2

	if P == 3:
		return g[0] + solve3(0, g[1], g[2])
		m = min(g[1], g[2])
		r1 = g[1] - m
		r2 = g[2] - m
		return g[0] + m + (r1 + 2) // 3 + (r2 + 2) // 3

	if P == 4:
		return g[0] + solve4(0, g[1], g[2], g[3])


testCases, = get()
for testCase in range(1, testCases+1):
	N, P = get()
	G = get()
	print('Case #{}: {}'.format(testCase, solve(N, P, G)))
