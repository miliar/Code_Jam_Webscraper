import fileinput

myfile = fileinput.input();
currentcase = 0
maxcases = 0

for line in myfile:
	if fileinput.isfirstline():
		maxcases = int(line.strip())
		continue

	currentcase += 1
	(r, t) = line.strip().split()

	r = int(r)
	t = int(t)

	# currentcircleminus1 = 0
	# while True:
	# 	t -= (2*r + 4*currentcircleminus1 + 1)
	# 	if t < 0:
	# 		break
	# 	currentcircleminus1+= 1

	# n = currentcircleminus1

	tworminus1 = 2*r - 1
	n = ((tworminus1**2 + 8*t)**(0.5) - tworminus1)/4

	print "Case #"+str(currentcase)+": "+str(int(n))

	if maxcases == currentcase:
		break