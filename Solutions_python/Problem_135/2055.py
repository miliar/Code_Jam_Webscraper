
T = input()

for t in range(1, T+1):
	r1 = input()-1

	m1 = [[None for _ in range(4)] for _ in range(4)]
	for i in range(4):
		m1[i] = map(int, raw_input().split())

	r2 = input()-1

	m2 = [[None for _ in range(4)] for _ in range(4)]
	for i in range(4):
		m2[i] = map(int, raw_input().split())

	s1, s2 = set(m1[r1]), set(m2[r2])

	s = s1.intersection(s2)

	print 'Case #%d:' % (t,),

	if len(s) == 1:
		print s.pop()
	elif len(s) > 1:
		print 'Bad magician!'
	else:
		print 'Volunteer cheated!'
