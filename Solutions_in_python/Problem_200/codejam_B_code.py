t = int(input())
for tt in range(1, t + 1):
	n = [int(c) for c in input().rstrip()]
	l = len(n)
	nines = False
	for i in range(l):
		if nines:
			n[i] = 9
		elif i < l - 1 and n[i] > n[i + 1]:
			n[i] -= 1
			nines = True
			for j in range(i, 0, -1):
				if n[j] < n[j - 1]:
					n[j] = 9
					n[j - 1] -= 1
	print("Case #%d: %s" % (tt, ''.join([str(n[i]) for i in range(1 if n[0] == 0 else 0, l)])))
