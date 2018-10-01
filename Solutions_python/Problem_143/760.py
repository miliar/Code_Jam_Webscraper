import sys


def main():

	fDataFile = open(sys.argv[1], 'r')

	sLine = fDataFile.readline()
	iNumTests = int(sLine)
	iItterations = 0
	while iItterations < iNumTests:

		sLine = fDataFile.readline()
		A = int(sLine.split(' ')[0])
		B = int(sLine.split(' ')[1])
		C = int(sLine.split(' ')[2])
		#print A, B, C
		iNumOfTotalCombinations = (A) * (B)
		iWinAttemps = 0

		for i in range(A-1, -1, -1):
			for j in range(B-1, -1, -1):
				binAND = i&j
				#print i, j, binAND

				if binAND < C:
					iWinAttemps += 1

		#print iWinAttemps
		print "Case #%d: %d" % ((iItterations+1), iWinAttemps)

		iItterations += 1
		#break

if __name__ == '__main__':
	main()