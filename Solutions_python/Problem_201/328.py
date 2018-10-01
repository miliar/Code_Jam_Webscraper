fin = open('C-large.in', 'r')
fout = open('C-large.out','w')






numlines = int(fin.readline().rstrip())

for line in range(numlines):
	vals = str(fin.readline().rstrip())
	(N,K) = tuple([int(c) for c in vals.split(" ")])
	
	splits = {N:1}
	minres = 0
	maxres = 0
	
	i = 0
	while i < K:
		j = max([v for v in splits if splits[v] != 0])
		
		if j % 2 == 1:
			minres = (j-1)/2
			maxres = (j-1)/2
		else:
			minres = (j-2)/2
			maxres = j/2
		
		i = i + splits[j]
		
		splits[minres] = (splits[minres] if minres in splits else 0) + splits[j]
		splits[maxres] = (splits[maxres] if maxres in splits else 0) + splits[j]
		splits[j] = 0
	
	result = str(maxres) + " " + str(minres)

	outstr = "Case #" + str(line+1) + ": " + str(result) + "\n"
	# print result.rstrip()
	fout.write(outstr)




