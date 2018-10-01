T = input()
for TC in range(1, T+1):
	S, K = raw_input().split()
	K = int(K)
	S = list(S)

	cnt = 0
	for i in range(len(S)-K+1):
		if S[i] == '-':
			for j in range(K):
				S[i+j] = '+' if S[i+j] == '-' else '-'
			cnt += 1
	
	if S.count('-') != 0:
		print "Case #{}: {}".format(TC, "IMPOSSIBLE")
	else:
		print "Case #{}: {}".format(TC, cnt)
