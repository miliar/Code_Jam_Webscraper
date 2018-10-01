import operator

t = int(input())

for case_num in range(t):
	line = [int(x) for x in input().split(' ')]
	n = int(line[0])
	k = int(line[1])
	u = float(input())
	p = [float(x) for x in input().split(' ')]
	p.sort()
	while u > 0:
		s0 = p[0]
		s1 = [(x, i) for i, x in enumerate(p) if x > s0]
		if len(s1) > 0:
			idx = s1[0][1]
			s1 = s1[0][0]
			if u >= (s1 - s0) * idx:
				for i in range(idx):
					p[i] += s1 - s0
				u -= (s1 - s0) * idx
			else:
				for i in range(idx):
					p[i] += u / idx
				u = 0
		else:
			p = [x + u / n for x in p]
			u = 0
	ans = 1
	for x in p:
		ans *= x
	print('Case #%d: %.8f' % (case_num + 1, ans))
