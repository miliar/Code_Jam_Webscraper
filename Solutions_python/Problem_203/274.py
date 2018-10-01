for cas in range(1, input()+1):
	r,c = map(int,raw_input().split())
	a=[raw_input() for i in range(r)]
	q = []
	for i in range(r):
		if set(a[i]) == set('?'):
			q.append(i)
			continue
		b=""
		curr=0
		for j in range(c):
			if a[i][j] == "?":
				curr += 1
			else:
				las = a[i][j]
				b += las * (curr + 1)
				curr = 0
		b += las * curr
		a[i] = b
	q.append(r)
	while len(q) > 1:
		for i in range(len(q) - 1):
			if q[i + 1] - q[i] != 1:
				a[q[i]] = a[q[i] + 1]
				q.remove(q[i])
				break
		else:
			q.remove(r)
			Q = len(q)
			for i in range(len(q)):
				a[q[i]] = a[r - Q - 1]
			q = []
		if len(q) == 2 and q[-2] == r-1:
			a[r-1] = a[r-2]
			break
	print "Case #%d:" % cas
	print "\n".join(a)