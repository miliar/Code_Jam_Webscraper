def panc(N,sp):
	output =0
	for i in xrange(0,len(N)-sp+1):
		if N[i]=='-':
			output+=1
			for j in range(0,sp):
				if N[i+j]=='-':
					N[i+j]='+'
				else:
					N[i+j]='-'
	for k in xrange(len(N)-sp+1,len(N)):
		if N[k]=='-':
			return "IMPOSSIBLE"
	return output; 



t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  n, m = [str(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
  print "Case #{}: {}".format(i, panc(list(n),int(m)))

