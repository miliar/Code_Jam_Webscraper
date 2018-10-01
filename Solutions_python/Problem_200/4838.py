f=list(map(int,open("tidy_numbers_small.txt").readlines()))
T=f[0]
for counter in range(1,T+1):
	N=f[counter]
	for i in range(N,0,-1):
		i=list(map(int,str(i)))
		out=[]
		for x in range(len(i[1:])):
			out.append(i[x+1]>=i[x])
		if all(out):
			print("Case #{}: {}".format(counter,''.join(map(str,i))))
			break