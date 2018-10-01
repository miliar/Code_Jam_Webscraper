def parser(filename):
	
	if not filename:
		filename = "A-small-attempt1.in"
	
	qinput = open(filename)
	aoutput = open('output1.txt', 'w')
	T = int(qinput.readline())
	string = '';

	for question in range(T):
		input = qinput.readline()
		C, F, X = tuple(map(lambda str: float(str), input.split()))
		string += "Case #" + str(question+1) + ": " + str(solver(C, F, X)) + "\n"

	aoutput.write(string)
	aoutput.close()
	qinput.close()


def solver(C, F, X):
	
	if (X < C):
		return X/2
	
	time0 = X/2
	numFarm = 0
	farmTime = 0

	while True:
		farmTime += C/(2 + F*numFarm)
		numFarm += 1
		time1 = farmTime + X/(2 + F*numFarm)
		if time1 > time0:
			return time0
		time0 = time1