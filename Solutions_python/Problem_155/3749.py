
testCases = input()
for i in range(testCases):
	people = 0
	inputList = []
	totalPeople = 0
	inputString = raw_input()
	maxShyness = int(inputString[0])
	inputString = inputString.split(' ')
	inputList = map(int, str(inputString[1]))
	
	for j in range(0, maxShyness+1):
		if(totalPeople<j):
			people+=j-totalPeople
			totalPeople+=j-totalPeople
		if(inputList[j]==0 and j==0):
			people+=1
			totalPeople+=1
		totalPeople+=inputList[j]
	print 'Case #{0}: {1}'.format(i+1, people)
