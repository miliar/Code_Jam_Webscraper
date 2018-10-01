import sys
import os

def solve(data):
	smax = int(data[0])
	crowds = [int(i) for i in list(data[1])]
	
	help = 0
	sum = 0
	for i in range(len(crowds)):
		bros = max(0, i - sum)
		help += bros
		sum += bros + crowds[i]
	return help



with open(sys.argv[1], 'r') as inputfile, open('ans.out','w') as outputfile:
	 inputfile.readline()
	 i = 1
	 for line in inputfile:
	 	outputfile.write('Case #%d: %d\n' % (i, solve(line.split())))
	 	i += 1


