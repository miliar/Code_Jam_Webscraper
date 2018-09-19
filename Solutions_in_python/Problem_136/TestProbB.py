import os

def parser(filename):
	testCases=[]
	with open(filename) as inFile:
		numTestCases=int(inFile.readline())
		for i in range(0,numTestCases):
			thisTestCase=inFile.readline().strip().split(" ")
			for elem in range(len(thisTestCase)):
				thisTestCase[elem]=float(thisTestCase[elem])
			testCases.append(thisTestCase)
	return testCases

def cookieAnswer(parsedData):
	iteration=1
	for elem in parsedData:
		cookiesPerSecond=2.0
		costFarm=elem[0]
		farmProduce=elem[1]
		winState=elem[2]
		numberFarms=0
		seconds=0.0

		#seconds+=1.0
		minimum=winState/2

		while(True):
			secondsToCostFarm=(costFarm)/(cookiesPerSecond+(numberFarms*farmProduce))
			winCalc = (winState)/(cookiesPerSecond+((numberFarms+1) * farmProduce))

			if (seconds+secondsToCostFarm+winCalc)>=minimum:
				break

			seconds+=secondsToCostFarm
			minimum=seconds+winCalc
			numberFarms+=1

		
		print("Case #"+str(iteration)+": "+str(minimum))
		iteration+=1

data = parser(os.sys.argv[1])
cookieAnswer(data)