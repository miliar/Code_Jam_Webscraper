file = open('input', 'r')

problems = int(file.readline())

def output(i, s):
	print "Case #" + str(i) + ":\n" + s

def output_field(x, array, r, c):
	count = 0
	print "Case #" + str(x) + ":"
	for i in range(0, r):
		row = ""
		for j in range(0, c):
			row = row + array[i][j]
			if array[i][j] == '*':
				count = count + 1
		print row
	return count

def init(R,C):
	gamefield = []
	for i in xrange(R):
		gamefield.append([])
		for j in xrange(C):
			gamefield[i].append('.')
	return gamefield

for x in range(1, problems+1):
	count = 0
	values = file.readline().split()	
	R = int(values[0])
	C = int(values[1])
	M = int(values[2])
	_M = M
	freeFields = R * C - M
	while True:
		if M == C * R - 1:
			gamefield = init(R, C)
			for a in range(0, R):
				for b in range(0, C):
					gamefield[a][b] = '*'
			gamefield[0][0] = 'c'
			count = output_field(x, gamefield, R, C)
			break
		if R == 1:
			gamefield = init(R, C)
			for a in range(0, M):
				gamefield[0][a] = '*'
			gamefield[0][C - 1] = 'c'
			count = output_field(x, gamefield, R, C)
			break
		if C == 1:
			gamefield = init(R, C)
			for a in range(0, M):
				gamefield[a][0] = '*'
			gamefield[R - 1][0] = 'c'
			count = output_field(x, gamefield, R, C)
			break
		if freeFields < 4: # could only be if R or C was 1, which is not the case!
			output(x, "Impossible")
			break
		if freeFields == 5 or freeFields == 7:
			output(x, "Impossible")
			break
		if R == 2:
			if  M % 2 == 1:
				output(x, "Impossible")
				break
			else:
				gamefield = init(R, C)
				for i in range(0, M / 2):
					gamefield[0][i] = '*'
					gamefield[1][i] = '*'
				gamefield[R - 1][C - 1] = 'c'
				count = output_field(x, gamefield, R, C)
				break
		if C == 2:
			if  M % 2 == 1:
				output(x, "Impossible")
				break
			else:
				gamefield = init(R, C)
				for i in range(0, M / 2):
					gamefield[i][0] = '*'
					gamefield[i][1] = '*'
				gamefield[R - 1][C - 1] = 'c'
				count = output_field(x, gamefield, R, C)
				break
		gamefield = init(R, C)		
		if C < R:
			for i in range(0, C - 3):
				if M > R:
					M = M - R
					for j in range(0, R):
						gamefield[j][i] = '*'
				else:	
					if M == R - 1:
						for j in  range(0, M - 1):
							gamefield[j][i] = '*'
						gamefield[0][i + 1] = '*'
					else:
						for j in  range(0, M):
							gamefield[j][i] = '*'
					M = 0		
					break
			if M == R:
				for a in  range(0, R):
					gamefield[a][C - 3] = '*'
			else:
				for j in range(0, R):
					if M <= 0: break
					if M == 1:
						gamefield[j][C - 3] = '*'
						break
					elif M == 2:
						gamefield[j][C - 3] = '*'
						gamefield[j + 1][C - 3] = '*'
						break
					elif M >= 3:
						gamefield[j][C - 3] = '*'
						gamefield[j][C - 2] = '*'
						gamefield[j][C - 1] = '*'
						M = M - 3
			gamefield[R - 1][C - 1] = 'c'
			count = output_field(x, gamefield, R, C)
			break
		else:
			for i in range(0, R - 3):
				if M > C:
					M = M - C
					for j in range(0, C):
						gamefield[i][j] = '*'
				else:	
					if M == C - 1:
						for j in  range(0, M - 1):
							gamefield[i][j] = '*'
						gamefield[i + 1][0] = '*'
					else:
						for j in  range(0, M):
							gamefield[i][j] = '*'
					M = 0		
					break
			if M == C:
				for a in range(0, C):
					gamefield[R - 3][a] = '*'
			else:
				for j in range(0, C):
					if M <= 0: break
					if M == 1:
						gamefield[R - 3][j] = '*'
						break
					elif M == 2:
						gamefield[R - 3][j] = '*'
						gamefield[R - 3][j + 1] = '*'
						break
					elif M >= 3:
						gamefield[R - 3][j] = '*'
						gamefield[R - 2][j] = '*'
						gamefield[R - 1][j] = '*'
						M = M - 3
			gamefield[R - 1][C - 1] = 'c'
			count = output_field(x, gamefield, R, C)
			break
	# print x, R, C, _M
	# print count
	# if count != _M:
	# 	print "WARNING!"
