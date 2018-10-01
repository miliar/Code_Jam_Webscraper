t = int(raw_input())  # read a line with a single integer
for p in xrange(1, t + 1):
	temp = raw_input().split(" ")
	inputlist = list(temp[0])
	k = int(temp[1])
	i=0
	count=0
	while i<len(inputlist):
		if inputlist[i]=='-':
			count+=1
			if i+k-1 < len(inputlist):
				for j in xrange(0,k):
					if inputlist[i+j]=='-':
						inputlist[i+j]='+'
					else:
						inputlist[i+j]='-'
		i+=1
	tag=True
	for i in xrange(0,len(inputlist)):
		if inputlist[i]=='-':
			print "Case #{}: IMPOSSIBLE".format(p)
			tag=False
			break
	if(tag):
		print "Case #{}: {}".format(p, count)
			

