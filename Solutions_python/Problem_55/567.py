import sys

in_file = open(sys.argv[1])
out_file = open("out.txt", 'w')

cases = int(in_file.readline().strip())
def read_case():
	R, k, N = (int(x) for x in in_file.readline().strip().split())
	g = [int(x) for x in in_file.readline().strip().split()]
	return R, k, N, g
	
for case in xrange(cases):
	R, k, N, g = read_case()
	position = 0
	euros = 0
	r = 0
	while r < R:
		if r > 0 and position == 0:
			repetitions = R // r
			if repetitions > 1:
				euros *= repetitions
				r *= repetitions
				if r >= R:
					break
		total = 0
		starting_at = position
		while total + g[position] <= k:
			total += g[position]
			position += 1
			if position == N:
				position = 0
			if position == starting_at:
				break
		euros += total
		r += 1
	out_file.write("Case #%d: %d\n" % (case+1, euros))