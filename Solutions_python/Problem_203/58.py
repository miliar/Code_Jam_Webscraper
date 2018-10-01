#! /usr/bin/python

T = int(raw_input())

for t in range(1, T+1):

	R, C = [int(inp) for inp in raw_input().split()]
	cake = [raw_input().strip() for _ in range(R)]
	
	hasLetter = [any([(cake[i][j] != '?') for j in range(C)]) for i in range(R)]

	for i in range(R):
		if hasLetter[i]:
			
			firstInd = 0
			while cake[i][firstInd] == '?':
				firstInd += 1

			lastLetter = cake[i][firstInd]
			for j in range(C):
				if cake[i][j] == '?':
					cake[i] = cake[i][:j] + lastLetter + cake[i][(j+1):]
				else:
					lastLetter = cake[i][j]

	firstRow = 0
	while hasLetter[firstRow] == False:
		firstRow += 1
	lastString = cake[firstRow]
	
	for i in range(R):
		if not hasLetter[i]:
			cake[i] = lastString
		else:
			lastString = cake[i]

	print 'Case #' + str(t) + ':'
	for i in range(R):
		print cake[i]
