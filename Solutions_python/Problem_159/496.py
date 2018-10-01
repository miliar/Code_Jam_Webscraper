f = open('A-large.in.txt', 'r')
T = int(f.readline())

for t in range(0,T):
	N = int(f.readline())
	line = f.readline().split()
	mush = map(int,line)

	methodone = 0
	previous = mush[0]
	for m in range(1,len(mush)):
		if (mush[m] < previous):
			methodone += (previous - mush[m])
		previous = mush[m]

	methodtwo = 0
	rate = 0
	prev = mush[0]
	for m in range(1,len(mush)):
		diff = prev - mush[m]
		if (diff > rate):
			rate = diff
		prev = mush[m]
	for m in range(0,len(mush)-1):
		if (mush[m] < rate):
			methodtwo += mush[m]
		else:
			methodtwo += rate

	print('Case #' + str(t+1) + ': ' + str(methodone) + ' ' + str(methodtwo))
	
f.close()