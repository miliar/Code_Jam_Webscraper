
def checkRow(row):
	if '.' in row:
		return -1

	result = True
	for i in xrange(1,4):
		compare = False
		if row[i] == row[i-1] or row[i] == 'T':
			compare = True
		result = result and compare
	if not result:
		return 0 

	i = 0 
	if row[0] == 'T':
		i = 1
	if row[i] == 'X':
		return 1
	if row[i] == 'O':
		return 2

def setStatus(check, status):
	winner = False
	if check == -1:
		status['complete'] = False
	if check == 1:
		status['winner'] = 'X'
		winner = True
	elif check == 2:
		status['winner'] = 'O'
		winner = True
	return status, winner

def readInput(filename):
	file = open(filename,'r')
	cases = []
	n = int(file.readline())
	for i in xrange(n):
		thisCase = {'complete':True,'winner':'T'}
		col = [['.']*4,['.']*4,['.']*4,['.']*4]
		diag = [['.']*4,['.']*4]
		foundWinner = False
		for j in xrange(4):
			line = list(file.readline().split('\n')[0])
			if not foundWinner:
				thisCase, foundWinner = setStatus(checkRow(line),thisCase)
				
				for k in xrange(4):
					col[k][j] = line[k]
				diag[0][j] = line[j]
 				diag[1][j] = line[3-j]
		if foundWinner:
			cases.append(thisCase)
		else:
			j = 0
			while not foundWinner and j < 4:
				thisCase, foundWinner = setStatus(checkRow(col[j]),thisCase)
				j += 1
			if not foundWinner:
				thisCase, foundWinner = setStatus(checkRow(diag[0]),thisCase)
			if not foundWinner:
				thisCase, foundWinner = setStatus(checkRow(diag[1]),thisCase)

			cases.append(thisCase)
		file.readline()
	file.close()
	return cases

def main():
	cases = readInput('A-small-attempt0.in')
	n = 1
	file = open('A-small-attempt0.out','w')
	for case in cases:
		if case['winner'] == 'T' and case['complete']:
			outStr = "Case #%i: Draw" % n
		if case['winner'] == 'X':
			outStr = "Case #%i: X won" % n
		if case['winner'] == 'O':
			outStr = "Case #%i: O won" % n
		if case['winner'] == 'T' and not case['complete']:
			outStr = "Case #%i: Game has not completed" % n
		file.write(outStr+'\n')
		n+=1
	file.close()

if __name__ == "__main__":
	main()