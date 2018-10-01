
def probA():
	filename = "A-small-attempt0.in.txt"
	f = open(filename)

	lines = f.readlines()

	cases, lines = int(lines[0]), lines[1:]
	results = []

	i, case = 0, 0
	while case < cases:
		answer1 = int(lines[i])
		row1 = set([int(x) for x in lines[i+answer1].split()])

		answer2 = int(lines[i+5])
		row2 = set([int(x) for x in lines[i+5+answer2].split()])

		possibleNums = row1.intersection(row2) # number must be common to both rows

		if len(possibleNums) == 0: 
			results.append("Volunteer cheated!") # no common numbers
		elif len(possibleNums) == 1: 
			results.append(possibleNums.pop()) # found the correct number
		else: 
			results.append("Bad magician!") # more than one possible number

		i += 10 # number of lines between cases
		case += 1

	writeResults(results)


def writeResults(results):
	outfile = open("probAResults.txt", "w")
	for i in range(1, len(results) + 1):
		outfile.write("Case #%i: %s\n" % (i, results[i-1]))
	outfile.close()



probA()
