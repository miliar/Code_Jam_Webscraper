#! /usr/bin/python

T = int(raw_input())

for t in range(1, T+1):

	caseData = raw_input().split()
	S = caseData[0]
	L = len(S)
	K = int(caseData[1])
	F = [0] * (L + K)

	currentFlip = False
	flipCount = 0
	canFlip = True
	for i in range(0, L):

		if F[i] == 1:
			currentFlip = not currentFlip

		if (S[i] == '-') ^ currentFlip:
			flipCount += 1
			F[i + K] += 1
			currentFlip = not currentFlip
			if i + K > L:
				canFlip = False

	if canFlip:
		print 'Case #' + str(t) + ': ' + str(flipCount)
	else:
		print 'Case #' + str(t) + ': ' + "IMPOSSIBLE"