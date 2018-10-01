X = "X won"
O = "O won"
D = "Draw"
G = "Game has not completed"
T = int(raw_input())
for cas in xrange(1, T + 1):
	print "Case #" + str(cas) + ":",
	row = list()
	col = list()
	diagonal = list()
	for i in xrange(0, 4):
		row.append(raw_input())
	for i in xrange(0, 4):
		col.append(row[0][i] + row[1][i] + row[2][i] + row[3][i])
	diagonal.append(row[0][0] + row[1][1] + row[2][2] + row[3][3])
	diagonal.append(row[0][3] + row[1][2] + row[2][1] + row[3][0])
	valid = row + col + diagonal
	if "XXXX" in valid:
		print X
	elif "OOOO" in valid:
		print O
	else:
		flag = False
		for s in valid: 
			if not "." in s:
				if not "O" in s:
					flag = True
					print X
					break
				if not "X" in s:
					flag = True
					print O
					break
		if not flag:
			print G if "." in "".join(valid) else D
	raw_input()
