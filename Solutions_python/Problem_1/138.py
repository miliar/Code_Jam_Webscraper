import sys
    
infile = sys.argv[1]
inp = open(infile)
outfile = sys.argv[2]
outp = open(outfile, "w")

num_cases = int(inp.readline())
i = 1
while i <= num_cases:
	num_switches = 0
	S = int(inp.readline().strip())
	for j in range(0, S) :
		inp.readline()
	Q = int(inp.readline().strip())
	q = []
	for j in range(0, Q) :
		engine = inp.readline().strip()
		if engine not in q :
			q.append(engine)
			if len(q) == S :
				q = [engine]
				num_switches += 1
	line = "Case #" + str(i) + ": " + str(num_switches)
	outp.write(line + '\n')
	i += 1

inp.close()
outp.close()
