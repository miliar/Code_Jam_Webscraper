

def main(fname, outName):
	result = ''
	with open(fname) as input:
		result = parse(input)

	output = open(outName, 'w')
	output.write(result)
	output.close()

def parse(input):
	output = ''

	caseCount = int(input.readline())
	for caseNum in range(caseCount):
		output += parseCase(caseNum+1, input)

	return output

def parseCase(caseNum, input):
	row1 = int(input.readline())-1
	board1 = getBoard(input)
	row2 = int(input.readline())-1
	board2 = getBoard(input)

	return getAnswer(caseNum, board1[row1]+board2[row2])


def getBoard(input):
	return [input.readline().strip().split(' ') for i in range(4)]

def getAnswer(caseNum, row):
	guess = set([x for x in row if row.count(x) > 1])
	answer = 'Volunteer cheated!'

	if len(guess) == 1:
		answer = guess.pop()
	elif len(guess) > 1:
		answer = 'Bad magician!'

	return 'Case #{0}: {1}\n'.format(caseNum, answer)




main('input.txt', 'out.txt')

