
def token():
	return raw_input()
def tokens():
	return raw_input().strip().split()

def solve(horses, dist, u, v):
	assert u == 0 and v == len(horses)-1
	N = len(horses)
	ts = [float('+inf')] * N
	ts[0] = 0
	# print N, ts
	for i, h in enumerate(horses):
		dm, s = h
		t0 = ts[i]
		d = 0
		j = i+1
		while j < N:
			d += dist[j-1][j]
			if d > dm:
				break
			t = t0 + float(d)/s
			if ts[j] > t:
				ts[j] = t
			j += 1
		# print ts
	return ts[-1]

for t in range(int(raw_input())):
	N, Q = map(int, tokens())
	T = 0
	horses = [map(int, tokens()) for i in range(N)] # (max dist, speed)
	dist = [map(int, tokens()) for i in range(N)] # N * N matrix, -1 if route is impossible
	res = []
	for i in range(Q):
		u, v = map(int, tokens())
		res.append(str(solve(horses, dist, u-1, v-1)))

	print "Case #{}: {}".format(t+1, ' '.join(res))
