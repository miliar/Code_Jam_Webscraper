def examine(layout1, row1, layout2, row2):
	intersection = layout1[row1 - 1] & layout2[row2 - 1]
	common = len(intersection)
	if common == 1:
		return str(next(iter(intersection)))
	elif common == 0:
		return 'Volunteer cheated!'
	else:
		return 'Bad magician!'

fin = open('A-small-attempt0.in', 'r')
fout = open('out.txt', 'w')
T = int(fin.readline())
for i in range(1, T + 1):
	row1 = int(fin.readline())
	layout1 = []
	for j in range(0, 4):
		layout1.append(set(int(x) for x in fin.readline().split()))
	row2 = int(fin.readline())
	layout2 = []
	for j in range(0, 4):
		layout2.append(set(int(x) for x in fin.readline().split()))
	answer = examine(layout1, row1, layout2, row2)
	fout.write('Case #' + str(i) + ': ' + answer + '\n')
fin.close()
fout.close()