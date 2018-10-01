def main():
	for TEST in range(1, int(input())+1):
		values = input().split()
		S = list(values[0])
		K = int(values[1])

		# print(S)
		# print(K)

		nFlips = 0
		for i in range(0, len(S)-K+1):
			c = S[i]
			if c == '-':
				for j in range(i, i+K):
					S[j] = '-' if S[j] == '+' else '+'
				nFlips += 1

		# print("".join(S))

		if all(c == '+' for c in S):
			result = str(nFlips)
		else:
			result = "IMPOSSIBLE"

		print("Case #%d: %s" % (TEST, str(result)))

main()
