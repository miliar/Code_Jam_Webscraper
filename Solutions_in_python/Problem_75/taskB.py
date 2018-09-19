from time import time
import sys

def parse(filein):
	fin = file(filein, 'r')
	cases = []
	numCases = int(fin.readline().strip())
	for line in fin:
		cases.append(Case(line))

	return cases

class Case(object):
	def __init__(this, line):
		this.parse(line)

	def parse(this, line):
		line = line.strip().split(' ')
		numCombines = int(line[0])
		this.parseCombines(line[1:1+numCombines])
		numOpposed = int(line[numCombines+1])
		this.parseOpposed(line[numCombines+2:numCombines+2+numOpposed])
		this.numElements = int(line[-2])
		this.elements = line[-1]

	def parseCombines(this, combines):
		this.combines = []
		for comb in combines:
			this.combines.append( (comb[:2],        comb[2]) )
			this.combines.append( (comb[1]+comb[0], comb[2]) )

	def parseOpposed(this, opposed):
		this.opposed = opposed[:]

	def reduceWithCombines(this, elements):
		lastPair = elements[-2:]
		for pair, form in this.combines:				
			if pair == lastPair:
				return elements[:-2]+form
		return None

	def reduceWithOpposed(this, elements):
		for opp in this.opposed:
			if opp[0] in elements and opp[1] in elements:
				return ""
		return elements

	def solve(this):
		curElements = this.elements[0]
		for char in this.elements[1:]:
			curElements += char
			reducedElements = this.reduceWithCombines(curElements)
			if reducedElements == None:
				curElements = this.reduceWithOpposed(curElements)
			else:
				curElements = reducedElements
		this.answer = curElements

	def pprint(this, i, fout):
		listOutput = ", ".join(this.answer)
		fout.write("Case #%d: [%s]\n"%(i, listOutput))

def main(filein, fileout):
	start = time()

	fout = file(fileout, 'w')
	cases = parse(filein)
	for i,x in enumerate(cases):
		x.solve()
		x.pprint(i+1, fout)

	fout.close()

	end = time()
	print "Total time=%s"%(end-start)

if __name__ == '__main__':
	main(sys.argv[1], sys.argv[2])
