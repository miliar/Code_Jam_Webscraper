def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False


def main():
	total = [];
	fin = open('A-small-attempt1.in')
	for line in fin:
		total += [line];
	
	testLenght = int(total[0])
	for i in range(0, testLenght):
		possibleVals = [];
		possibleVals = [total[int(total[1+(i*10)])+1+(i*10)]]
		newVals = [total[int(total[6+(i*10)])+6+(i*10)]]
		newNewVals = newVals[0].split(" ")
		newnewnewvals = []

		for aVal in newNewVals:
			newnewnewvals += [int(aVal)]

		valCounnt = 0
		for aVal in possibleVals[0].split(" "):
			if(RepresentsInt(aVal)):
				if(int(aVal) in newnewnewvals):
					valCounnt += 1
					successVal = aVal;
		if(valCounnt == 0):
			print "Case #"+str(i+1)+": Volunteer cheated!"
		if(valCounnt > 1):
			print "Case #"+str(i+1)+": Bad magician!"
		if(valCounnt == 1):
			print "Case #"+str(i+1)+ ": " + str(successVal)

if __name__ == '__main__':
	main()

