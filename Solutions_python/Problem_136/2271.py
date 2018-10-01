from sys import argv
file = argv[1]
fi = open(file)
ab = open("small.in", "w")
cases = int(fi.readline().strip("\n"))
tot_time, pers = 0.0, 2.0

for y in xrange(cases):
	c, f, x = fi.readline().strip("\n").split(" ")
	c, f, x = float(c), float(f), float(x)
	print c, f, x
	while True:
		if (x/(pers))<=((c/pers) + (x/(pers+f))):
			tot_time = tot_time + x/pers
			break
		else:
			tot_time += c/pers
			pers += f
	ab.write("Case #" + str(y+1) + ": " + str(tot_time)+ "\n")
	tot_time = 0.0
	pers = 2.0