def solve(N):
	s = len(N)
	N = list(N)

	for i in range(s):
		index = s - i - 1
		if index > 0:
			right = int(N[index])
			left = int(N[index - 1])
			if left > right:
				N[index-1] = str(left - 1)
				N[index:] = "9" * len(N[index:])
	return int( "".join(N))

T = int( raw_input())

for i in range(T):
	N = raw_input()
	res = solve(N)
	res_line = "Case #" + str(i + 1) + ": "
	res_line += str( res)
	print res_line