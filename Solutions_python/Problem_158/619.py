import math

inputFile = open('D-small-attempt0.in', 'r')
inString = inputFile.read()
inputLines = inString.split('\n')
inputLines.pop(0)
inputLines.pop()
output = ''
case = 1

idealShapeProfileMap = {1: (1, 1), 2: (2, 1), 3: (2, 2), 4: (2, 3)}
for line in inputLines:
	relevantLine = map(int, line.split(' '))
	print relevantLine
	shapeArea = relevantLine[0]
	minShapeDimension = int(math.ceil(shapeArea / 2.0))
	shapeProfile = idealShapeProfileMap[shapeArea]
	gridWidth = relevantLine[1]
	gridHeight = relevantLine[2]
	gridArea = (gridWidth * gridHeight)
	shapeWins = False
	# omino produces hole
	if shapeArea > 6:
		shapeWins = True
	# grid not evenly divisible by omino size
	elif gridArea % shapeArea != 0:
		shapeWins = True
	# omino's minimum dimension won't fit in grid's minimum
	elif minShapeDimension > min(gridWidth, gridHeight):
		shapeWins = True
	# omino fits into grid producing an area that cannot be filled
	elif shapeArea == 4 and gridArea < shapeArea * shapeArea and min(gridWidth, gridHeight) == minShapeDimension:
		shapeWins = True
	winner = 'GABRIEL'
	if shapeWins:
		winner = 'RICHARD'
	output += ('Case #' + str(case) + ': ' + winner+ '\n')
	case += 1
	
outputFile = open('out1.out', 'w')
outputFile.write(output)
