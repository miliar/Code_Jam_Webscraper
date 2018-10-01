(L,D,N) = raw_input().split(' ')
L = int(L)
D = int(D)
N = int(N)

words = []
for i in xrange (0, D):
	words.append(raw_input())

for query in xrange (0, N):
	qraw = raw_input ()

	single = True
	q = list()
	for c in qraw:
		if c == '(':
			single = False
			q.append([])
		elif c == ')':
			single = True
		else:
			if single:
				q.append(c)
			else:
				q[len(q)-1].append(c)

	counter = 0
	for word in words:
		valid = True
		ndex = 0
		try:
			for char in word:
				if char in q[ndex]:
					ndex+=1
				else:
					valid = False
					break
		except Exception:
			valid = False
		if valid: counter += 1
	print 'Case #%d: %d' % (query+1,counter)
