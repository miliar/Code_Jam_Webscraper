f = open('A-large.in', 'r')
o = open('output', 'w')

num = f.readline() # num

for lineIndex, line in enumerate(f):
	line = line.strip() # remove newline character
	splitLine = line.split(" ")
	max = splitLine[0]
	totalPeople = 0
	numberToAdd = 0
	for index, char in enumerate(splitLine[1]):
		peopleNeeded = 0
		if (totalPeople < index):
			peopleNeeded = (index) - totalPeople
			numberToAdd = numberToAdd + peopleNeeded
		totalPeople = totalPeople + peopleNeeded + int(char)  # Everyone before this level + people needed to get on THIS level + people on this level
	o.write("Case #" + str(lineIndex+1)   + ": " + str(numberToAdd) + "\n")
	print("Case #" + str(lineIndex+1) + ": " + str(numberToAdd))
o.close()