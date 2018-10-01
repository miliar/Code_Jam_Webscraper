def flip(S, flag, K):
	d = {'+' : '-', '-' : '+'}
	return ''.join(list(S[: flag]) + [d[x] for x in S[flag : flag+K]] + list(S[flag+K :]))

def find_flips(S, K, case_num):
	flips = 0
	if '-' not in S:
		flips = 0
	else:
		while '-' in S and S.index('-') + K <= len(S):
			flag = S.index('-')			
			S = flip(S, flag, K)
			flips += 1
	if '-' not in S:
		print "Case #{}: {}".format(case_num, flips)
	else:
		print "Case #{}: {}".format(case_num, 'IMPOSSIBLE')	


T = int(raw_input())  # read a line with a single integer
for case_num in xrange(1, T + 1):
  S, K = raw_input().split(' ')
  K = int(K)
  find_flips(S, K, case_num)
  # check out .format's specification for more formatting options
