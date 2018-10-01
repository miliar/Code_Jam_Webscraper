def solve(S, K):
	all_flips = [False for i in xrange(len(S))]
	total_flips = 0
	cur_pancake_flipped = False
	for i in xrange(len(S)):
		if i >= K:
			cur_pancake_flipped ^= all_flips[i-K]
		pancake_needs_flip = S[i] == '-'
		if cur_pancake_flipped ^ pancake_needs_flip:
			if i+K > len(S):
				return "IMPOSSIBLE"
			all_flips[i] = True
			total_flips += 1
			cur_pancake_flipped = not(cur_pancake_flipped)
	return total_flips


T = int(raw_input())
for case in xrange(1, T+1):
	S, K = raw_input().split()
	print "Case #{}: {}".format(case, solve(S, int(K)))

