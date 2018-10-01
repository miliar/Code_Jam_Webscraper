f = open("A-small-attempt0.in", "r")
o = open("Bullseye-A-small-attempt0-out.txt", "w")
T = int(f.readline())




for t in range(T):
	count = 0
	randt = f.readline().split()
	r = int(randt[0]) #white circle radius
	paint = int(randt[1]) #mL of paint
	rIn = r
	rOut = r + 1
	nextArea = rOut**2 - rIn**2
	
	while paint >= nextArea:
		count += 1
		paint -= nextArea
		rOut += 2
		rIn += 2
		nextArea = rOut**2 - rIn**2
		
	o.write("Case #" + str(t+1) + ": " + str(count) + "\n")

f.close()
o.close()
