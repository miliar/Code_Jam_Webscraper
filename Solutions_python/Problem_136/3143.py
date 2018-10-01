def cookies(case): 
	farmCost = float(case[0])
	farmRate = float(case[1])
	target = float(case[2])

	#c30, r1, x2 
	time = 0 
	rate = 2.0

	while target/rate > farmCost/rate + target/(rate+farmRate):
		time += farmCost/rate 
		rate += farmRate
	else: 
		time += target/rate

	return time

if __name__ == "__main__":
	f = open('/Users/stefsy/code/codejam2014/cookieslarge.in','r')
	num_cases = int(f.readline())
	cases = []
	for line in f: 
		c = []
		v = line.strip('\n').split(" ")
		for u in v: 
			u = float(u)
			c.append(u)
		cases.append(c)
	f.close()

	for x in range(0,len(cases)): 
		print "Case #" + str(x+1) +": " + str(cookies(cases[x]))
