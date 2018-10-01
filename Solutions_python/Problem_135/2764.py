with open('A-small-attempt0.in', 'r') as fin:
	with open('A-small-practice.out.txt', 'w') as fout:
		n = int(fin.readline())
		for i in range(n):
			ans1 = int(fin.readline())
			for r in range(4):
				if r == ans1-1:
					row1 = set([int(x) for x in fin.readline().split()])
				else:
					fin.readline()
			ans2 = int(fin.readline())
			for r in range(4):
				if r == ans2-1:
					row2 = set([int(x) for x in fin.readline().split()])
				else:
					fin.readline()
			ints = row1 & row2
			if len(ints) == 1:
				fout.write('Case #' + str(i + 1) + ': ' + str(list(ints)[0]) + '\n')
			elif len(ints) == 0:
				fout.write('Case #' + str(i + 1) + ': Volunteer cheated!\n')
			elif len(ints) > 1:
				fout.write('Case #' + str(i + 1) + ': Bad magician!\n')