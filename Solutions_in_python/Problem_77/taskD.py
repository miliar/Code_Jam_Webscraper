import sys
from time import time

def parse(filein):
	fin = file(filein, 'r')
	cases = []

	numcases = int(fin.readline().strip())

	for i in range(numcases):
		countNumbers = int(fin.readline().strip())
		values = map(int, fin.readline().strip().split(' '))
		cases.append(Case(values))

	return cases

class Case(object):
	def __init__(this, values):
		this.values = values

	def solve(this):
		answer = 0
		for i, value in enumerate(this.values):
			if i+1!=value:
				answer+=1
		this.answer = answer

	def pprint(this, i, out):
		out.write("Case #%d: %.6f\n"%(i, this.answer))


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
