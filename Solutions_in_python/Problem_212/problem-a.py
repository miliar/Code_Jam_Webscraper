
def token():
	return raw_input()
def tokens():
	return raw_input().strip().split()

def solve(N, P, groups):
	counts = [0] * P
	for g in groups:
		counts[g % P] += 1
	res = counts[0]
	if P == 2:
		res += (counts[1]+1) / 2
		return res
	if P == 3:
		g1, g2 = counts[1:]
		a, b = g1, g2
		if a < b:
			a, b = b, a
		res += b
		res += (a-b+2) / 3
		return res
	if P == 4:
		g1, g2, g3 = counts[1:]
		res += g2 / 2
		g13 = min(g1, g3)
		res += g13
		g13 = max(g1, g3) - g13
		if g2 % 2 == 1:
			res += 1
			g13 -= 2
		if g13 > 0:
			res += (g13 + 3) / 4
		return res

for t in range(int(raw_input())):
	N, P = map(int, tokens())
	groups = map(int, tokens())
	res = solve(N, P, groups)
	print "Case #{}: {}".format(t+1, res)
