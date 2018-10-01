fin = open('A-large.in', 'r')
fout = open('A-large.out','w')






numlines = int(fin.readline().rstrip())

for line in range(numlines):
	vals = str(fin.readline().rstrip())
	(S,K) = tuple([c for c in vals.split(" ")])
	
	S = [c for c in S]
	K = int(K)
	flips = 0
	
	for i in range(len(S)-K+1):
		if S[i] == "-":
			flips = flips + 1
			for j in range(K):
				S[i+j] = "+" if (S[i+j] == "-") else "-"
	
	if all([c == "+" for c in S]):
		result = str(flips)
	else:
		result = "IMPOSSIBLE"

	outstr = "Case #" + str(line+1) + ": " + str(result) + "\n"
	# print result.rstrip()
	fout.write(outstr)




