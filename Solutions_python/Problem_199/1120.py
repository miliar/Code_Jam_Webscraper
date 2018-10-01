for cas in range(1, input()+1):
	s,k=raw_input().split()
	k,ans=int(k),0
	while True:
		while len(s) and s[0] == '+':
			s = s[1:]
		if len(s) == 0:
			print "Case #%d: %d" % (cas, ans)
			break
		elif len(s) < k:
			print "Case #%d: IMPOSSIBLE" % cas
			break
		else:
			ans += 1
			temp = ""
			for i in range(k):
				temp += '+' if s[i] == '-' else '-'
			s = temp + s[k:]