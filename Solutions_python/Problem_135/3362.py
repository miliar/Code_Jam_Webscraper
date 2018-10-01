n = int(raw_input())

for k in range(1, n + 1):	
	l1 = int(raw_input())
	l1 -= 1

	r1 = []
	for i in range(4):
		aux = map(int, raw_input().split())	
		if i == l1:
			r1 = aux

	l2 = int(raw_input())
	l2 -= 1

	r2 = []
	for i in range(4):
		aux = map(int, raw_input().split())	
		if i == l2:
			r2 = aux

	s = []
	for e in r2:
		if e in r1:
			s.append(e)

	if len(s) == 0:
		s = "Volunteer cheated!"
	elif len(s) == 1:
		s = str(s[0])
	else:
		s = "Bad magician!"

	print "Case #" + str(k) + ": " + s