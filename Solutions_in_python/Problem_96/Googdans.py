basefilename = 'B-large'
infilename = basefilename+'.in'
outfilename = basefilename+'.out'

def main():
	# Utils
	resultlist = []
	N = 0

	# Take input
	infile = open(infilename, 'Ur')
	N = int(infile.readline())
	casenum = 0
	for line in infile:
		# DO IT
		N, S, p = line.split()[0:3]
		N, S, p = int(N), int(S), int(p)
		
		# Supprisingly least possible = p + p -2 + p -2
		suplpos = (3 * p) -4

		# Unspurisingly least possible = p + p - 1 + p -1
		unsuplpos = p + p - 1 + p -1

		totals = [int(score) for score in line.split()[3:]]

		resline = 0
		numsups = 0
		for total in totals:
			if total >= unsuplpos:
				resline += 1
			elif suplpos > 0 and total >= suplpos:
				numsups += 1
				if numsups <= S:
					resline += 1
		
		casenum += 1
		resultlist.append("Case #"+ str(casenum)+": "+str(resline)+"\n")

	# Write output	
	outfile = open(outfilename, 'w')
	outfile.writelines(resultlist)

	# Lets close this
	infile.close()
	outfile.close()

if __name__ == "__main__":
	main()

