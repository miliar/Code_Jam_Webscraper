if __name__ == '__main__':
	f = open('A-large.in', 'r')
	g = open('output.out', 'w')
	numCases = int(f.readline())

	caseNum = 0
	for line in f:
		caseNum += 1
		words = line.split()
		maxShyness = int(words[0])
		totalPeople = 0
		friends = 0
		for i in range(maxShyness + 1):
			numPeople = int(words[1][i])
			if numPeople == 0 and totalPeople <= i:
				friends += 1
				totalPeople += 1
			else:
				totalPeople += numPeople
		g.write('Case #' + str(caseNum) + ': ' + str(friends) + '\n')


	f.closed
	g.closed


