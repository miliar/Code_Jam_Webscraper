import operator


cases = int(raw_input())

for case in range(cases):

	N, R, O, Y, G, B, V = [int(o) for o in raw_input().split()]

	nArray = []
	last = ''
	valDict = {'B':B, 'Y':Y, 'R':R}
	while 1:

		henk = False

		tmp = sorted(valDict.items(), key=operator.itemgetter(1))
		#print tmp
		#print nArray
		for nextLatest in reversed(tmp):
			#print nextLatest
			
			if nextLatest[0] == last:
				continue
			else:
				if nextLatest[1] <= 0:
					henk = True
					break

				if len(nArray) > 0 and nArray[0] != last and nArray[0] != nextLatest[0] and valDict[nArray[0]] == valDict[nextLatest[0]]:
					nArray.append(nArray[0])
					last = nArray[0]
					valDict[nArray[0]] -= 1
					henk = False
					break
				else:
					nArray.append(nextLatest[0])
					last = nextLatest[0]
					valDict[nextLatest[0]] -= 1
					henk = False
					break

		if henk:
			break

	#print valDict

	answer = ''.join(nArray)
	if valDict['Y'] > 0 or valDict['R'] > 0 or valDict['B'] > 0:
		answer = "IMPOSSIBLE"

	if 'BB' in answer or 'YY' in answer or 'RR' in answer or answer[0] == answer[-1]:
		answer = "IMPOSSIBLE"

	if answer != 'IMPOSSIBLE':
		assert len(answer) == N
		assert answer.count('B') == B
		assert answer.count('R') == R
		assert answer.count('Y') == Y


	print "Case #" + str(case+1) + ": " + answer