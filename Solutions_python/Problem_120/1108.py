def bullseye(myfile):
	f = open(myfile, "r")
	g = open("file13.out", "w")
	numExamples = int(float(f.readline()))
	k = 1
	while (k < numExamples+1):
		radius, paint = f.readline().split()
		radius = float(radius)
		paint = float(paint)
		# paint first white circle
		whiteCircleArea = (radius**2)
		numOfBlackRings = 0
		areaToDraw = 0.0
		while(paint > 0):
			radius += 1
			# paint black ring
			areaToDraw = (radius**2)
			areaToDraw -= whiteCircleArea
			paint -= areaToDraw
			if (paint < 0):
				break
			# paint white ring
			radius += 1
			whiteCircleArea = (radius**2)
			numOfBlackRings += 1
		g.write("Case #" + str(k) + ": " + str(numOfBlackRings) + "\n")	
		k += 1
	f.close()
	g.close()

print bullseye('A-small-attempt0.in')
