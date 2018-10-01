import sys

infile = sys.argv[1]
outfile = sys.argv[2]

inf = open(infile)
outf = open(outfile, 'w')

numTestCases = inf.readline()

def readTestCase(casenum):
	candidates = []
	rownumber = int(inf.readline())
	for i in range(1, 5):
		row = inf.readline().split()
		if i == rownumber:
			candidates = row
	rownumber = int(inf.readline())
	currentCandidate = ''
	found = False
	morethanone = 0
	for i in range(1, 5):
		row = inf.readline().split()
		if i == rownumber:
			for item in row:
				if item in candidates:
					currentCandidate = item
					# sys.stdout.write('Case #1: ' + item + '\n')
					found = True
					morethanone += 1
	if morethanone > 1:
		outf.write('Case #' + casenum + ': Bad magician! \n')
	elif found == False:
		outf.write('Case #' + casenum + ': Volunteer cheated! \n')
	else:
		outf.write('Case #' + casenum + ': '+ currentCandidate +' \n')


for i in range(0, int(numTestCases)):
	readTestCase(str(i+1))