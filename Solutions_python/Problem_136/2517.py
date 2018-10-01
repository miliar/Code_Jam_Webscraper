lines = list(open('B-large.in.txt','r'))
output = open('B-large.out.txt','w')
attemps = int(lines[0])
for attemp in range (0,attemps):
	dataset = list(lines[attemp + 1].split())
	c = float(dataset[0])
	f = float(dataset[1])
	x = float(dataset[2])
	cps = 2
	minimum = (x/cps)
	seconds = (c/cps)
	cps += f
	next_minimum = (x/cps) + seconds
	while (next_minimum < minimum):
		minimum = next_minimum
		seconds += (c/cps)
		cps += f
		next_minimum = (x/cps) + seconds
	output.write("Case #" + str(attemp + 1) + ": " + str(round(minimum,7)) + "\n")
