def main():
	T = int(raw_input())
	for t in range(T):
		R, C = [int(x) for x in raw_input().split()]
		cake = [[x for x in raw_input()] for _ in range(R)]
		found = [False for i in range(R)]
		for i in range(R):
			for j in range(C):
				if cake[i][j] != '?':
					found[i] = True
					
					k = j-1
					while k >= 0 and cake[i][k] == '?':
						cake[i][k] = cake[i][j]
						k -= 1
					
					k = j+1
					while k < C and cake[i][k] == '?':
						cake[i][k] = cake[i][j]
						k += 1

		for i in range(R):
			if not found[i]:
				index = -1
				for j in range(i-1, -1, -1):
					if found[j]:
						index = j
						break

				if index == -1:
					for j in range(i+1, R, 1):
						if found[j]:
							index = j
							break

				for j in range(C):
					cake[i][j] = cake[index][j]

		print 'Case #%d:' % (t+1)
		for i in range(R):
			print ''.join(x for x in cake[i])

main()