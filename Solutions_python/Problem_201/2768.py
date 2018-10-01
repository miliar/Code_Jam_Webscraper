T = int(input())
for t in range(1, T + 1):
	result = ""
	N, K  = [int(i) for i in input().split(" ")]
	if N == K:
		result = "{} {}".format(0, 0)
	else:
		s = [0 for i in range(N)]
		for c in range(K):
			Ls = [0 for i in range(N)]
			Rs = [0 for i in range(N)]
			for i in range(N):
				if s[i] == 0:
					try:
						Ls[i] = s[i::-1].index(1) - 1
					except ValueError:
						Ls[i] = i
					try:
						Rs[i] = s[i+1:].index(1)
					except ValueError:
						Rs[i] = N - i - 1
			mini = [min(Ls[i], Rs[i]) if s[i] == 0 else -1 for i in range(N)]
			minimum = max(mini)
			minIndex = [i for i in range(N) if mini[i] == minimum]	
			maxi = [max(Ls[i], Rs[i]) if i in minIndex else -1 for i in range(N)]
			maxIndex = maxi.index(max(maxi))
			maximum = max(maxi)
			if len(minIndex) == 1:
				s[minIndex[0]] = 1
			else:
				s[maxIndex] = 1
			result = "{} {}".format(maximum, minimum)
	
	print("Case #{}: {}".format(t, result))