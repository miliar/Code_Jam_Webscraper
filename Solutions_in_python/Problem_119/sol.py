for t in xrange(1, int(raw_input()) + 1):
	print "Case #%d:" % t,
	k, n = map(int, raw_input().split())
	keys = []
	keys.append(map(int, raw_input().split()))
	for i in xrange(n):
		keys.append(map(int, raw_input().split()))
	dp = {}
	kn = {}
	for i in keys[0]:
		if i not in kn:
			kn[i] = 0
		kn[i] += 1
	def rek(m):
#		print m, "\t", kn
		if m in dp:
			return dp[m]
		for i in xrange(n):
			if m & (1 << i) == 0 and keys[i + 1][0] in kn and kn[keys[i + 1][0]] > 0:
				kn[keys[i + 1][0]] -= 1
				for j in keys[i + 1][2:]:
					if j not in kn:
						kn[j] = 0
					kn[j] += 1
				if rek(m | (1 << i)) != -1:
					dp[m] = i + 1
					return i + 1
				for j in keys[i + 1][2:]:
					kn[j] -= 1
				kn[keys[i + 1][0]] += 1
		dp[m] = -1
		return -1 if m < (1 << n) - 1 else 0
	if (rek(0)) == -1:
		print "IMPOSSIBLE"
	else:
		q = 0
		for i in xrange(n):
			print rek(q),
			q |= (1 << (rek(q) - 1))
		print