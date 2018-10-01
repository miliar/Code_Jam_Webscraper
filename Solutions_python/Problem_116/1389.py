def checkWin(checkStr):
	#print "Checking: ", checkStr

	x_count = checkStr.count("X")
	o_count = checkStr.count("O")
	t_count = checkStr.count("T")
	
	#print "x: %d, o: %d, t: %d" %(x_count, o_count, t_count)

	if (x_count == 4) or (x_count == 3 and t_count == 1):
		#print "Result: x"
		return 'x'
	elif (o_count == 4) or (o_count == 3 and t_count == 1):
		#print "Result: o"
		return 'o'
	else:
		#print "Result: ."
		return '.'


filename = 'A-large.in'
file = open(filename, 'r')
lines = file.read().splitlines()
numTests = int(lines[0])

index = 0
for testNum in range(numTests):

	rows = ["", "", "", ""]
	cols = ["", "", "", ""]
	diags = ["", ""]
	completed = True
	Xwon = False
	Owon = False

	for i in range(4):
		index += 1
		row_str = lines[index]
		rows[i] = row_str
		dot_count = row_str.count(".")

		if completed == True and dot_count > 0:
			completed = False

		#print "Row_str, len: %s, %d" %(row_str, len(row_str))
		for j in range(4):
			#print "j", j
			cols[j] += row_str[j]

		diags[0] += row_str[i]
		diags[1] += row_str[3-i]

	#process all lines
	allLines = rows + cols + diags
	for line in allLines:
		result = checkWin(line)
		if result == 'x':
			Xwon = True
			break
		elif result == 'o':
			Owon = True
			break

	resultString = ""
	if Xwon:
		resultString = "X won"
	elif Owon:
		resultString = "O won"
	elif completed:
		resultString = "Draw"
	else:
		resultString = "Game has not completed"

	print "Case #%d: %s" %(testNum+1, resultString)
	index += 1


