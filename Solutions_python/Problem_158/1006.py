with open("D-small-attempt1.in") as input:
	T = int(input.readline())
	for i in xrange(T):
		data = list(map(int, input.readline().split(' ')))
		X = data[0]
		R = data[1]
		C = data[2]
		result = "GABRIEL"
		if (R * C) % X != 0:
			result = "RICHARD"
		elif (X - min(R,C)) > min(R,C):
			result = "RICHARD"
		elif X > 6:
			result = "RICHARD"
		elif X > 3 and min(R,C) < 3:
			result = "RICHARD"
		print("Case #"+str(i+1)+": "+str(result))