import collections

for t in range(int(input())):
	n, k = (int(i) for i in input().split())
	c = {n: 1}
	l = collections.deque([n])
	while k > c[l[0]]:
		v = l.popleft()
		k -= c[v]
		res = v // 2
		if v % 2:
			if res in c:
				c[res] += c[v] * 2
			else:
				c[res] = c[v] * 2
				l.append(res)
		else:
			if res in c:
				c[res] += c[v]
			else:
				c[res] = c[v]
				l.append(res)
			if res - 1 in c:
				c[res - 1] += c[v]
			else:
				c[res - 1] = c[v]
				l.append(res - 1)
		del c[v]
	v = l[0]
	res = v // 2
	if v % 2:
		print("Case #%d: %d %d" % (t + 1, res, res))
	else:
		print("Case #%d: %d %d" % (t + 1, res, res - 1))