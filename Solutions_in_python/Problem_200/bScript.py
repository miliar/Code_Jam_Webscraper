#!/usr/bin/python

fo = open("B-small-attempt1.in", "r")

# Get number of test cases
numTest = int(fo.readline())

#construct  an array of input
testCases = []

i = 0
while i < numTest:
    testCases.append(str(int(fo.readline())))
    i = i + 1


print "Test Cases are %s", testCases
fi = open("output", "w") 

iter = 1

# Loop through testCases array
for tc in testCases:
	#print tc
	index = tc
	while not all(index[i] <= index[i + 1] for i in xrange(len(index)-1)):
		index = str(int(index)-1)
	else:
		 print index
		 fi.write("Case #" + str(iter) + ":  " + index + "\n")
		 iter = iter+1

		



