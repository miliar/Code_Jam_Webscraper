import sys

def testLine(i, lawn, height):
	for item in lawn[i]:
		if item > height:
			return False
	return True

def testColumn(j, lawn, height):
	for line in lawn:
		if line[j] > height:
			return False
	return True

##########################################################
# Main

inputFileName = sys.argv[1]

f = file(inputFileName)
fout = file("output.txt", "w")

T = eval(f.readline())

for case in xrange(T):
	data = f.readline().split()
	N = eval(data[0])
	M = eval(data[1])
	possible = True
	if N == 1 or M == 1:
		for i in xrange(N):
			f.readline()
	else:
		lawn = []
		for i in xrange(N):
			line = f.readline().strip().split()
			for j in xrange(M):
				line[j] = eval(line[j])
			lawn.append(line)
		i = 0
		while i < N and possible:
			for j in xrange(M):
				if not testLine(i, lawn, lawn[i][j]):
					if not testColumn(j, lawn, lawn[i][j]):
						possible = False
			i += 1

	##### Output writing
	fout.write("Case #%d: " %(case + 1))
	if possible:
		fout.write("YES\n")
	else:
		fout.write("NO\n")
