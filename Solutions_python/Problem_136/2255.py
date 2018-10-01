# Google Code Jam 2014
# Qualification Round
# Problem B. Cookie Clicker Alpha
#
# Kevin Yap (@iKevinY)
# http://kevinyap.ca

import sys

def clicker(farmCost, farmOutput, win):
	cookieGen = 2
	timeElapsed = 0

	# gg ez duel
	if win < farmCost:
		return timeElapsed + win / cookieGen

	while True:
		waitTime = win / cookieGen
		farmTime = (farmCost / cookieGen) + (win / (cookieGen + farmOutput))
		if waitTime < farmTime: # Tests if shorter to wait or to buy farm and then wait
			return timeElapsed + waitTime
		else:
			timeElapsed += (farmCost / cookieGen)
			cookieGen += farmOutput




if __name__ == '__main__':
    inputFile = file(sys.argv[1])
    outputFile = file("output.txt", "w+")
    testCases = int(inputFile.readline())

    for n in range(0, testCases):
    	farmCost, farmOutput, win = [float(x) for x in inputFile.readline().split()]
    	outputFile.write("Case #{0}: {1}\n".format(n + 1, clicker(farmCost, farmOutput, win)))
