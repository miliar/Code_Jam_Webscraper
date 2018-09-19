import math

def Sort(sizes):
	for i in range(len(sizes)):
		for j in range(len(sizes) - 1):
			if sizes[j] > sizes[j+1]:
				tmp = sizes[j]
				sizes[j] = sizes[j+1]
				sizes[j+1] = tmp
	return sizes
	
def printCases(result):
	for i in range(len(result)):
		print "Case #" + str(i+1) + ": " + str(result[i])
