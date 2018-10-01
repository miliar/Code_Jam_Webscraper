def read_case(f):
	n = int(f.readline())
	matr = []
	for j in range(4):
		matr.append(list(map(int,f.readline().split())))
	return (n, matr)


def compare_rows(f):
	r1, m1 = read_case(f)
	r2, m2 = read_case(f)

	old = m1[r1-1]
	new = m2[r2-1]
	diff = []
	for ind, el in enumerate(new):
		if el in old:
			diff.append(ind)

	if len(diff) == 0:
		return 'Volunteer cheated!'
	elif len(diff) == 1:
		return str(new[diff[0]])
	elif len(diff) > 1:
		return 'Bad magician!'
	
res = []
with open('A-small-attempt0.in','r') as f:
	n = int(f.readline())
	for i in range(n):
		print('Case #{0}: {1}'.format(i+1, compare_rows(f)))

		
