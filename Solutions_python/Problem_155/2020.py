import sys
debug = True
debug = False
def console(line):
	if(debug):
		print line

fileName = sys.argv[1]
f = open(fileName,"r")
testCase = int(f.readline())
# print testCase
for i in range(testCase):
	console(i)
	sMax,people = f.readline().split()
	# print sMax,people
	mySum = 0
	level = 0
	needNum = 0
	for num in people:
		myNum = int(num)
		if(mySum >= level):
			mySum += myNum
		else:
			#not enough people
			needNum += level - mySum
			mySum = level + myNum
		level += 1
		# print num
	# print needNum
	print "Case #"+str(i+1)+": "+str(needNum)

	



