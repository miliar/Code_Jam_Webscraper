
IN_PATH = 'in/A-small-attempt0.in'
OUT_PATH = 'out/output.txt'


f = open(IN_PATH)
output = open(OUT_PATH, 'w')
t = int(f.readline())


for i in xrange(t):
	both_row_selections = []

	for b in xrange(2):
		row_selection = int(f.readline())

		for g in xrange(4):
			if row_selection == g + 1:
				both_row_selections.append(f.readline().split())
			else:
				f.readline()


	compare = set(both_row_selections[0]) & set(both_row_selections[1])
	if len(compare) == 1:
		output.write('Case #%s: ' % (i+1) + compare.pop() + '\n')

	elif len(compare) > 1:
		output.write('Case #%s: ' % (i+1) + 'Bad magician!'+ '\n')

	elif len(compare) == 0:
		output.write('Case #%s: ' % (i+1) + 'Volunteer cheated!'+ '\n')

output.close()
f.close()