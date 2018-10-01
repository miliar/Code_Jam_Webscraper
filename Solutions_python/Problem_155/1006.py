import sys

trace = True

def trace(string):
	if(trace):
		print(string)


def additionalFriends(audArr):
	currentClapping = 0
	numberOfNewFriends = 0

	for i in (xrange(len(audArr))):
		if (currentClapping >= i):
			currentClapping += int(audArr[i])
		elif(int(audArr[i]) > 0):
			numberOfNewFriends += i - currentClapping
			currentClapping += i - currentClapping + int(audArr[i])

	return numberOfNewFriends 

def runTest(l):

	l = l.split()

	Smax = int(l[0])
	numAddFriends = additionalFriends(list(l[1]), Smax)

	return numAddFriends
	

def runTesting():

	assert(additionalFriends(list('11111')) == 0)
	assert(additionalFriends(list('09')) == 1)
	assert(additionalFriends(list('110011')) == 2)
	assert(additionalFriends(list('1')) == 0)
		
if __name__ == '__main__':

	if (len(sys.argv) < 2):
		runTesting()
		sys.exit()

	else: 
		filename = sys.argv[1]
		f = open(filename, 'r')

	testCases = int(f.next())
	caseNum = 0

	for l in f:
		l = l.split()

		caseNum += 1
		Smax = int(l[0])

		numAddFriends = additionalFriends(list(l[1]))


		print('Case #' + str(caseNum) + ': %s' % numAddFriends)


		
