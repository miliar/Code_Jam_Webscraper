cases = int(input())

res = []

for case in range(1, cases+1):
	inp = int(input())
	if inp < 10:
		res.append((case, inp))
		continue
	for i in range(inp, 0, -1):
		t = list(str(i))
		if t == sorted(t):
			res.append((case, ''.join(t)))
			break

for i in res:
	print('Case #',i[0], ': ', i[1], sep='')