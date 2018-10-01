# Google CodeJam 2011, Part C: Magicka

def checkCombinations(index, elements):
	for combination in combinations:
		if ((elements[index] in combination[0] and elements[index - 1] in combination[1]) or 
			(elements[index] in combination[1] and elements[index - 1] in combination[0])):
			elements[index - 1] = combination[2]
			elements.pop(index)
			return True
	return False

def checkOpposites(index, elements):
	for opposite in opposites:
		for element in elements:
			if ((elements[index] in opposite[0] and element in opposite[1]) or 
				(elements[index] in opposite[1] and element in opposite[0])):
				return True
	return False
	
f = open('B-large.in', 'r')
out = open('output.txt', 'w')
cases = int(f.readline())

for i in range(1, cases + 1):
	combinations = []
	opposites = []
	elements = []
	lineRemaining = f.readline()
	partitioned = lineRemaining.partition(' ')
	count, lineRemaining = int(partitioned[0]), partitioned[2]
	for x in range(0, count):
		partitioned = lineRemaining.partition(' ')
		combinations.append(partitioned[0])
		lineRemaining = partitioned[2]
		
	partitioned = lineRemaining.partition(' ')
	count, lineRemaining = int(partitioned[0]), partitioned[2]
	for x in range(0, count):
		partitioned = lineRemaining.partition(' ')
		opposites.append(partitioned[0])
		lineRemaining = partitioned[2]
		
	partitioned = lineRemaining.partition(' ')
	count, lineRemaining = int(partitioned[0]), partitioned[2]
	for x in lineRemaining:
		elements.append(x)
		length = len(elements) - 1
		if length > 0:
			if not checkCombinations(length, elements):
				if checkOpposites(length, elements):
					elements = []
	
	try:
		elements.remove('\n')
	except ValueError:
		None
	
	out.write("Case #%d: %s\n" % (i, str(elements).replace("'", "")))
	
out.close
f.close()

