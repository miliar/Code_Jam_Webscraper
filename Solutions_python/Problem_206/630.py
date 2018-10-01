## 
def cruise(D,horses):
	time = 0
	horses = sorted(horses , key=lambda k: k[0])
	horses.append([D,0])
	N = len(horses) - 1

	while horses[0][0] < D:
		catchtime = [None]*N
		for i in range(N):
			gap = (horses[i+1][0] - horses[i][0])*1.0
			relspeed = (horses[i][1] - horses[i+1][1])*1.0
			if relspeed > 0:
				catchtime[i] = gap/relspeed
			else:
				catchtime[i] = (D - horses[i][0])*1.0/horses[i][1] 
		mincatchtime = min(catchtime)

		while mincatchtime in catchtime:
			j = catchtime.index(mincatchtime)
			del catchtime[j]
			del horses[j]
			N = N - 1
		for i in range(N):
			horses[i][0] = horses[i][0] + horses[i][1]*mincatchtime
		time = time + mincatchtime

	return D*1.0/time		



print cruise(2525,[[2400,5]])
print cruise(300,[[120,60],[60,90]])
print cruise(100,[[80,100],[70,10]])



## I/O Handler
fIn = open('A_1.txt', 'r')
fOut = open('A_1_sol.txt','w+')
nCases = int(fIn.readline())
for i in range(nCases):
	t = fIn.readline()
 	D, N = t.split(" ")
 	D = int(D)
 	N = int(N)
 	horses = [[None,None] for j in range(N)] # Initialize horses
 	for j in range(N):
 		t = fIn.readline()
 		pos, speed = t.split(" ")
 		horses[j][0] = int(pos)
 		horses[j][1] = int(speed)
 	ans = cruise(D,horses)
 	output = "Case #{}: {}\n".format(i+1,ans)
 	fOut.write(output)
fIn.close
fOut.close


