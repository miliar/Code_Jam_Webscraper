import sys

combine = []
oppose = []
invoke = []

def initCase(words):
	global combine
	global oppose
	global invoke
	del combine[:]
	del oppose[:]
	del invoke[:]

	index = 0
	numCombine = int(words[index])
	for i in range(index + 1, index + numCombine + 1):
		combine.append(list(words[i]))
		
	index += numCombine + 1
	numOppose = int(words[index])
	for i in range(index + 1, index + numOppose + 1):
		oppose.append(list(words[i]))
		
	index += numOppose + 2
	invoke = list(words[index])

def solveCase():
	global combine
	global oppose
	global invoke

	elements = []
	for i in invoke:
		elements.append(i)
		length = len(elements)
		if length >= 2:
			startNewCombine = 1
			while startNewCombine == 1:
				startNewCombine = 0
				for j in range(len(combine)):
					if sorted(elements[-2:]) == sorted(combine[j][:-1]):
						elements = elements[:-2] + combine[j][-1:]
						startNewCombine = 1
			for j in range(len(oppose)):
				found = 1
				for k in oppose[j]:
					temp = elements[:]
					if k in temp:
						temp.remove(k)
					else:
						found = 0
					if found == 0:
						break
				if found == 1:
					del elements[:]
					break
	
	return elements
	
fileIn = open(sys.argv[1], "r")
fileOut = open("B-large.out", "w")

def listString(list):
	s = "["
	for i in range(len(list)):
		if i != len(list) -1:
			s += list[i] + ", "
		else:
			s += list[i]
	s += "]"
	return s

num = 0
for line in fileIn:
	if num != 0:
		words = line.strip().split(" ")
		initCase(words)
		fileOut.write("Case #" + str(num) + ": " + listString(solveCase()) + "\n")
	num += 1
	
fileIn.close()
fileOut.close()