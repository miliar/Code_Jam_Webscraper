import math

def getNumMins(array):
	array.sort(reverse=True)
	x = array[0]

	if x <= 2:
		return x

	a = math.ceil(array[0] / 2.0)
	b = math.floor(array[0] / 2.0)
	array.pop(0)
	array.append(int(a))
	array.append(int(b))
	array.sort(reverse=True)
	y = 1 + getNumMins(array)

	return min(x, y)


if __name__ == '__main__':
	f = open('B-large.in', 'r')
	g = open('output.out', 'w')
	numCases = int(f.readline())

	caseNum = 0
	while True:
		caseNum += 1

		line1 = f.readline()
		if line1 == '':
			break
		line2 = f.readline()
		D = int(line1)
		array = [int(c) for c in line2.split()]
		
		numMins = max(array)

		numMinsTemp = 2
		while numMinsTemp < numMins:
			numMinsAfterDiv = sum([(elem - 1) // numMinsTemp for elem in array]) + numMinsTemp
			numMins = min(numMins, numMinsAfterDiv)
			numMinsTemp += 1

		g.write('Case #' + str(caseNum) + ': ' + str(int(numMins)) + '\n')


	f.closed
	g.closed


