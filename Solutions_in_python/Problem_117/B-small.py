def checkRight(lawnLst, i, j, height, width, dist):
	#print 'width', width
	#print 'dist', dist, 'j + dist', j + dist, 'width - 1', width - 1
	if j + dist > width - 1:
		#print 'Right true i', i, 'j', j, 'dist', dist
		return True
	elif lawnLst[i][j] >= lawnLst[i][j + dist]:
		return checkRight(lawnLst, i, j, height, width, dist + 1)
	else:
		#print 'Right False i', i, 'j', j, 'dist', dist
		return False

def	checkLeft(lawnLst, i, j, height, width, dist):
	if j - dist < 0:
		#print 'left true i', i, 'j', j, 'dist', dist
		return True
	elif lawnLst[i][j] >= lawnLst[i][j - dist]:
		return checkLeft(lawnLst, i, j, height, width, dist + 1)
	else:
		#print 'checkLeft lawnLst[i][j]', lawnLst[i][j], 'lawnLst[i][j - dist]', lawnLst[i][j - dist]
		#print 'left False i', i, 'j', j, 'dist', dist
		return False

def checkTop(lawnLst, i, j, height, width, dist):
	if i - dist < 0:
		#print 'top true i', i, 'j', j, 'dist', dist
		return True
	elif lawnLst[i][j] >= lawnLst[i - dist][j]:
		return checkTop(lawnLst, i, j, height, width, dist + 1)
	else:
		#print 'checkTop lawnLst[i][j]', lawnLst[i][j], 'lawnLst[i - dist][j]', lawnLst[i - dist][j]
		#print 'top False i', i, 'j', j, 'dist', dist
		return False

def	checkBottom(lawnLst, i, j, height, width, dist):
	if i + dist > height - 1:
		#print 'bottom true i', i, 'j', j, 'dist', dist
		return True
	elif lawnLst[i][j] >= lawnLst[i + dist][j]:
		return checkBottom(lawnLst, i, j, height, width, dist + 1)
	else:
		#print 'checkBottom lawnLst[i][j]', lawnLst[i][j], 'lawnLst[i + dist][j]', lawnLst[i + dist][j]
		#print 'bottom False i', i, 'j', j, 'dist', dist
		return False

def checkHorizontal(lawnLst, i, j, height, width):
	right = checkRight(lawnLst, i, j, height, width, 1)
	if right:
		left = checkLeft(lawnLst, i, j, height, width, 1)
		return left
	else:
		return False

def checkVertical(lawnLst, i, j, height, width):
	top = checkTop(lawnLst, i, j, height, width, 1)
	if top:
		bottom = checkBottom(lawnLst, i, j, height, width, 1)
		return bottom
	else:
		return False

def checkAllSides(lawnLst, height, width):
	for i in range(0, height):   
			for j in range(0, width):
				#print 'i', i, 'j', j
				horizontal = checkHorizontal(lawnLst, i, j, height, width)
				if horizontal:
					continue
				else:
					vertical = checkVertical(lawnLst, i, j, height, width)
					if vertical:
						continue
					else:
						return False
	return True

#f = open('sample.txt', 'r')
#f = open('test.txt', 'r')
f = open ('B-small-attempt1.in', 'r')
#f = open('A-large-practice.in', 'r')
f2 = open('output.txt', 'a')

inputNumber = 1
firstFlg = 1
lawnLst = []
width = 0
height = 0

for line in f:
	line = line.split()
	lst = []
	for n in line:
		lst.append(int(n))
	if firstFlg:
		numOfInput = lst[0]
		firstFlg = 0
	elif (len(lawnLst) == height):
		height = lst[0]
		width = lst[1]
		#print 'height', height
		#print 'width', width
		lawnLst = []
	else:
		lawnLst.append(lst)
		if (len(lawnLst) == height):
			result = checkAllSides(lawnLst, height, width)
			if result:
				answer = 'YES'
			else:
				answer = 'NO'
			f2.write('Case #' + str(inputNumber) + ': ' + answer + '\n')
			inputNumber = inputNumber + 1

f2.close()
f.close()
	
