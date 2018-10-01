#! /usr/bin/python

from math import sqrt

def simple(P, Q):
	for i in range(3, P + 1, 2):
		while P%i == Q%i == 0:
			P /= i
			Q /= i
	return (P, Q)

if __name__ == "__main__":
	outputFile = open("A.out", "w")
	#data = [[int(numStr) for numStr in line.split()] for line in open("A.in", "r")]
	data = [[int(numStr) for numStr in line.split('/')] for line in open("A.in", "r")]
	numOfCase = data[0][0]
	dataIndex = 1
	for caseIndex in range(numOfCase):
		P = data[caseIndex + 1][0]
		Q = data[caseIndex + 1][1]
		(P, Q) = simple(P, Q)
		print P, Q

		result = ""
		if Q & (Q - 1) != 0:
			result = 'impossible'
		else:
			num = 1
			while P < Q / 2:
				num += 1
				P *= 2
			result = str(num)

		outputLine = "Case #%d: %s\n" % (caseIndex + 1, result)
		print outputLine
		outputFile.write(outputLine)
	outputFile.close()
