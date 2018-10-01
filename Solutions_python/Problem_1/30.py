if __name__ == "__main__":
	N = int(raw_input())
	for test in range(N):
		engines = []
		queries = []
		E = int(raw_input())
		for i in range(E):
			engines.append(raw_input())
		Q = int(raw_input())
		for i in range(Q):
			queries.append(raw_input())
		s = 0
		res = 0
		while s < Q:
			next = -1
			for i in range(E):
				for j in range(s, Q + 1):
					if j == Q or queries[j] == engines[i]:
						next = max(next, j)
						break
			s = next
			res += 1
		print "Case #%d: %d" % (test + 1, max(0, res - 1))
