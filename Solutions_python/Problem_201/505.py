def dists(N, k):
	state = {N:1}
	while True:
		new_state = {}
		x = max(state.keys())
		if x == 0:
			break
		cnt = state[x]
		del state[x]
		state[x/2]=state.get(x/2, 0) + cnt
		state[(x-1)/2] = state.get((x-1)/2, 0) + cnt
		k -= cnt
		if k <= 0:
			return (x/2, (x-1)/2)

def win(inp, outp):
	lines = open(inp, 'rb').readlines()
	res = []
	for line in lines[1:]:
		if line[-1:] == '\n':
			line = line[:-1]
		N, k = map(int, line.split(' '))
		res.append(dists(N, k))
	out = []
	for i in xrange(len(res)):
		out.append('Case #{}: {} {}'.format(str(i + 1), res[i][0], res[i][1]))
	f = open(outp, 'wb')
	f.write('\n'.join(out))
	f.close()

win("/Users/Dan/Desktop/codejam/Ci3.in", '/Users/Dan/Desktop/codejam/Co3.txt')