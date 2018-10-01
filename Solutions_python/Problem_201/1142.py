for cas in range(1, input()+1):
	n,k=map(int,raw_input().split())
	taken=[False]*(n+2)
	ls=[0]*(n+2)
	rs=[0]*(n+2)
	taken[0]=True
	taken[-1]=True
	ls[0] = -1
	ls[-1] = -1
	rs[0] = -1
	rs[-1] = -1
	for i in range(k):
		for j in range(1, n+1):
			ls[j] = -1 if taken[j] else (ls[j-1] + 1)
		for j in range(n, 0, -1):
			rs[j] = -1 if taken[j] else (rs[j+1] + 1)
		currmax, currans=0,[]
		for j in range(1, n+1):
			if min(ls[j], rs[j]) > currmax:
				currmax = min(ls[j], rs[j])
				currans = [j]
			elif min(ls[j], rs[j]) == currmax:
				currans.append(j)
		if len(currans) == 1:
			taken[currans[0]] = True
			curr = currans
			continue
		currmax, curr = 0, []
		for j in currans:
			if max(ls[j], rs[j]) > currmax:
				currmax = min(ls[j], rs[j])
				curr = [j]
			elif max(ls[j], rs[j]) == currmax:
				curr.append(j)
		taken[curr[0]] = True
	ans = curr[0]
	print "Case #%d: %d %d" % (cas, max(ls[ans], rs[ans]), min(ls[ans], rs[ans]))