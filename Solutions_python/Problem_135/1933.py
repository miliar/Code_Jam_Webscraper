def getboard():
	a = []
	for i in range(4):
		a += [map(int, raw_input().split())]
	return a

T = int(raw_input())

for test in xrange(T):
	i = int(raw_input())
	b = getboard()
	cand1 = set(b[i - 1])

	i = int(raw_input())
	b = getboard()
	cand2 = set(b[i - 1]) 

	res = ''
	ans = cand1.intersection(cand2)

	if len(ans) == 0:
		res = 'Volunteer cheated!'
	elif len(ans) > 1:
		res = 'Bad magician!'
	else:
		res = str(ans.pop())

	print 'Case #%d: %s' % (test + 1, res)
