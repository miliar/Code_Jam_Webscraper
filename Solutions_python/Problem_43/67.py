T = int(raw_input())
for T_count in range(T):
	line = raw_input().strip()
	a = set(line)
	base = len(a)
	if base <= 1:
		base = 2
	b = dict()
	b[line[0]] = 1
	count = 0
	ans = 0
	for i in range(len(line)):
		if not b.has_key(line[i]):
			b[line[i]] = count
			count = count + 1
			if count == 1:
				count = 2
		ans = ans + b[line[i]]*(base**(len(line) - i - 1))
	print 'Case #%d: %d' % (T_count + 1, ans)

