inputData = open("B-large.in").read().split("\n")[1:-1]

outputFile = open("output.txt", "w+")

for i in range(len(inputData)):
	c = float(eval(inputData[i].split(" ")[0]))
	f = float(eval(inputData[i].split(" ")[1]))
	x = float(eval(inputData[i].split(" ")[2]))
	n = 0.0
	t = 0.0
	r = 2.0
	while (x > n):
		if ( (x - n)/r > (c/r + (x-n)/(r+f)) ):
			
			t = t + c/r
			r = r+f
		else:
			
			t = t +  (x - n)/r
			n = x
	
	outputFile.write("Case #" + str(i+1) + ": " + str(round(t, 7)) + "\n")

outputFile.close()
