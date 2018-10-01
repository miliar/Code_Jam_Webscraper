from sys import stdin
from collections import defaultdict

for cs in xrange(1,1+int(stdin.readline().strip())):
	tttt = [[z for z in stdin.readline().strip()] for zz in xrange(4)]
	stdin.readline()
	
	# for r in tttt:
	# 	for ch in r:
	# 		print ch,
	# 	print
	# print

	rows = [defaultdict(int) for x in xrange(4)]
	cols = [defaultdict(int) for x in xrange(4)]
	tldiag = defaultdict(int)
	brdiag = defaultdict(int)

	dots=0
	for row in xrange(4):
		for col in xrange(4):
			ch = tttt[row][col]
			rows[row][ch] +=1
			cols[col][ch] +=1
			if(row==col):
				tldiag[ch] += 1
			if(row+col==3):
				brdiag[ch] += 1

	alllines=rows
	alllines.extend(cols)
	alllines.append(tldiag)
	alllines.append(brdiag)

	result=None
	complete = True
	for line in alllines:
		limit = 4 - line["T"]
		if line["O"] >= limit:
			result="O won"
			break
		if line["X"] >= limit:
			result="X won"
			break
		if line["."] > 0:
			complete = False

	# print "Won? {} Complete? {}".format(result, str(complete))

	if(result):
		sol = result
	elif complete:
		sol = "Draw"
	else:
		sol = "Game has not completed"

	print "Case #" + str(cs) + ": " + sol




