# Author Gavin Brown
# Google Code Jam 2014 Round 1B problem B:

infile = open('input.in', 'r')
outfile = open('output.out','w')
numCases = int(infile.readline())
for case in range(numCases):
	result = 0
	args = infile.readline().split()
	A = int(args[0])
	B = int(args[1])
	K = int(args[2])
	for a in range(A):
		for b in range(B):
			if a & b < K:
				result +=1

	


	outfile.write("Case #{0}: {1}\n".format(case+1, result))
infile.close()
outfile.close()

