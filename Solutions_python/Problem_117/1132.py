def checkSquare(lawn, dims, square):
	canMowRow = True
	height = lawn[square[0]][square[1]]
	for col in range(dims[1]):
		if lawn[square[0]][col] > height:
			canMowRow = False
			break
	if canMowRow:
		return True
	
	canMowCol = True
	for row in range(dims[0]):
		if lawn[row][square[1]] > height:
			canMowCol = False
			break
	if canMowCol:
		return True
	
	return False

def readLawn():
	dim_str = input().split()
	rows = int(dim_str[0])
	cols = int(dim_str[1])
	lawn = []
	for i in range(rows):
		row_str = input().split()
		lawn.append([])
		for j in range(cols):
			lawn[i].append(int(row_str[j]))
	return ((rows, cols), lawn)

nCases = int(input())
case = 0
while case < nCases:
	case += 1
	text = "Case #{0}: {1}"
	(dims, lawn) = readLawn()
	allMown = True
	for i in range(dims[0]):
		for j in range(dims[1]):
			if not checkSquare(lawn, dims, (i, j)):
				allMown = False
				break
	if not allMown:
		print(text.format(case, "NO"))
	else:
		print(text.format(case, "YES"))