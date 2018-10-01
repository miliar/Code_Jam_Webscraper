T = int(raw_input())

for t in range(T):
	line = raw_input().split()
	N = int(line[0])
	C = int(line[1])
	files = raw_input().split()
	for i in range(len(files)):
		files[i] = int(files[i])
	files.sort()
	j = len(files)-1
	i = 0
	res = 0
	while (i < j):
		if (files[i] + files[j] > C):
			j-=1
		else:
			j-=1
			i+=1
		res += 1
	if i == j:
		res+=1
	print "Case #%d: %d"%(t+1, res)
		
