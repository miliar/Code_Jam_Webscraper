file = open('input', 'r')

problems = int(file.readline())

for z in range(1, problems+1):
	wins = 0
	values = file.readline().split()
	A = int(values[0])
	B = int(values[1])
	K = int(values[2])
	for i in range(0, A):
		for j in range(0, B):
			if (i&j) < K:
				wins += 1
	print "Case #" + str(z) + ": " + str(wins)
