def getInput(prob):
	f = open(prob, "r")
	answer = []
	cases = int(f.readline())
	for i in range(cases):
		temp = []
		for i in range(4):
			l = f.readline()
			temp.append(list(l.replace("\n", "")))
			
		f.readline()
		answer.append(temp)
	f.close()
	return answer

def main(prob, ans):
	inp = getInput(prob)
	answer = []
	for case in inp:
		answer.append(solveCase(case))
	writeToFile(answer, ans)

def solveCase(case):
	for row in case:
		l = analyzeInp(row)
		if l == "X":
			return "X won"
		elif l == "O":
			return "O won"
		elif l == False:
			continue
	for column in getColumns(case):
		l = analyzeInp(column)
		if l == "X":
			return "X won"
		elif l == "O":
			return "O won"
		elif l == False:
			continue
	for diagonal in getDiagonals(case):

		l = analyzeInp(diagonal)
		if l == "X":
			return "X won"
		elif l == "O":
			return "O won"
		elif l == False:
			continue		

	if '.' in getLinear(case):
		return "Game has not completed"
	else:
		return "Draw"

def analyzeInp(ar):
	default = None
	if ar[0] == 'T':
		default = ar[1]
	else:
		default = ar[0]

	for i in ar:
		if i != default:
			if i != 'T':
				return False
		else:
			continue
	else:
		return default

def getColumns(case):
	columns = []
	for i in range(4):
		columns.append([case[j][i] for j in range(4)])
	return columns

def getLinear(case):
	answer = []
	for i in case:
		for j in i:
			answer.append(j)
	return answer

def writeToFile(answer, answerFile):
	f = open(answerFile, "w")
	for i in range(len(answer)):
		temp = "Case #" + str(i + 1) + ": " + answer[i]
		f.write(temp + "\n")
	f.close()

def getDiagonals(case):
	answer = []
	answer.append([case[i][i] for i in range(4)])
	temp = []
	j = 0
	for i in range(3, -1, -1):
		temp.append(case[j][i])
		j += 1
	answer.append(temp)	
	
	return answer

# print(getDiagonals([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]))
# print(getDiagonals([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]))	
# print(getInput("problemSample.txt"))
print(main("large.in", "answerLarge.txt"))




