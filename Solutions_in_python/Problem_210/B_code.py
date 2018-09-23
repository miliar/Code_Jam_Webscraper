def care(cam,jam):
	c = len(cam)
	j = len(jam)
	cam = sorted(cam, key=lambda k: k[0])
	jam = sorted(jam, key=lambda k: k[0])	
	

	if c == 2: 
		if cam[1][1] - cam[0][0] <= 720:
			return 2
		elif cam[0][1] + 1440 - cam[1][0] <= 720:
			return 2
		else:
			return 4

	if j == 2: 
		if jam[1][1] - jam[0][0] <= 720:
			return 2
		elif jam[0][1] + 1440 - jam[1][0] <= 720:
			return 2
		else:
			return 4

	return 2


## I/O Handler
fIn = open('B_0.txt', 'r')
fOut = open('B_0_sol.txt','w+')
nCases = int(fIn.readline())
for i in range(nCases):
	t = fIn.readline()
 	c, j = t.split(" ")
 	c = int(c)
 	j = int(j)
 	cam = [[None,None] for k in range(c)] # Initialize
 	jam = [[None,None] for k in range(j)] 
 	for k in range(c):
 		t = fIn.readline()
 		start, end = t.split(" ")
 		cam[k][0] = int(start)
 		cam[k][1] = int(end)
 	for k in range(j):
 		t = fIn.readline()
 		start, end = t.split(" ")
 		jam[k][0] = int(start)
 		jam[k][1] = int(end)
 	ans = care(cam,jam)
 	output = "Case #{}: {}\n".format(i+1,ans)
 	fOut.write(output)
fIn.close
fOut.close


