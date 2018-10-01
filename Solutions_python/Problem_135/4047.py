infile = open("A-small-attempt0.in", "r")
totaltests = int(infile.readline())
for testnum in range(0, totaltests):
	firstsquare = []
	secondsquare = []

	firstchoice = int(infile.readline())
	for rownum in range(0, 4):
		values = infile.readline().rstrip().split(' ')
		firstsquare.append(values)
	
	secondchoice = int(infile.readline())
	for rownum in range(0, 4):
		values = infile.readline().rstrip().split(' ')
		secondsquare.append(values)
	
	possibilities = [x for x in firstsquare[firstchoice - 1] if x in secondsquare[secondchoice - 1]]
	
	if len(possibilities) == 1:
		result = possibilities[0]
	elif len(possibilities) == 0:
		result = "Volunteer cheated!"
	elif len(possibilities) > 1:
		result = "Bad magician!"
	else:
		print("ERROR")
	
	print("Case #{}: {}".format(testnum + 1, result))
	