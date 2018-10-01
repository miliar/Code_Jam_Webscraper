def solve(horse, matrix, s, e):

	h = [horse[s - 1]]
	time = [0]
	while (s != e):
		i = 0
		while i < len(h):
			h[i][0] -= matrix[s - 1][s]
			if (h[i][0] < 0):
				h = h[:i] + h[i + 1:]
				time = time[:i] + time[i + 1:]
				continue
			time[i] += matrix[s - 1][s] / h[i][1]
			i += 1
		s += 1
		if (s != e):
			time.append(min(time))
			h.append(horse[s - 1])
	print '{:.6f}'.format(min(time))



def _main():
	n, q = raw_input().split(' ')
	n = int(n)
	q = int(q)
	horse = []
	for i in range(0, n):
		e, s = raw_input().split(' ')
		horse.append([float(e), float(s)])
	matrix = []
	for i in range(0, n):
		l = raw_input().split(' ')
		line = []
		for elem in l:
			if float(elem) == -1:
				line.append(False)
			else:
				line.append(float(elem))
		matrix.append(line)
	point = []
	for i in range(0, q):
		u, v = raw_input().split(' ')
		point.append((int(u), int(v)))
	for elem in point:
		s, e = elem
		solve(horse, matrix, s, e)



nbTest = int(raw_input())
for i in range(1, nbTest + 1):
	print "Case #"+ str(i) + ":",
	_main()