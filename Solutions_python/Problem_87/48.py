input = open("Airport Walkways.in")
output = open("Airport Walkways.out", "w")
T = int(input.readline())

for t in range(T):
	X, S, R, tt, N = [int(a) for a in input.readline().split(" ")]
	walkways = []
	W = 0
	for w in range(N):
		walkways.append(list(reversed([int(a) for a in input.readline().split(" ")])))
		W += walkways[-1][1] - walkways[-1][2]
	NW = X - W
	walkways.append([0, NW, 0])
	walkways = sorted(walkways)
	TT = 0
	for w in walkways:
		d = w[1] - w[2]
		rd = min(d, tt * (w[0] + R))
		tt -= rd / (w[0] + R)
#		print(tt)
		TT += rd / (w[0] + R) + (d - rd) / (w[0] + S)
	print("Case #{case}: {result:0.6f}".format(case = t + 1, result = TT), file = output)
