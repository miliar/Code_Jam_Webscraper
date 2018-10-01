



def solve(infile, outfile):
	answersFile = open(outfile, 'w')
	f = open(infile, 'r')
	cases = int(f.readline().replace('\n',''))
	for case_number in xrange(cases):
		sets = []
		for turn in xrange(2):
			line_number = int(f.readline().replace('\n',''))  - 1
			for i in xrange(4):
				line = f.readline().replace('\n','')
				if i == line_number:
					sets.append(set([ int(x) for x in line.split(" ") ]))
		ans = list(sets[0].intersection(sets[1]))

		casing = "Case #" + str(case_number+1) + ": "
		if len(ans) == 0:
			answersFile.write(casing + "Volunteer cheated!\n")
		elif len(ans) == 1:
			answersFile.write(casing + str(ans[0]) + "\n")
		else:
			answersFile.write(casing + "Bad magician!\n")
	f.close()
	answersFile.close()
	return

if __name__ == "__main__":
	import sys

	if not len(sys.argv) == 2:
		print "python solver.py input output"
		sys.exit()

	solve(sys.argv[1]+".in", sys.argv[1]+".out")

