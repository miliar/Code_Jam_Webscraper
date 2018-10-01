f = file("A-small-attempt0.in")
#f = file("A-large.in")
#f = file("test.in")
of = file("A-small-attempt0.out", "w")
#of = file("A-large.out")
#of = file("test.out", "w")

def calc(trees):
	result = 0
	for t1 in range(len(trees)):
		for t2 in range(t1 + 1, len(trees)):
			for t3 in range(t2 + 1, len(trees)):
				print "try:", t1, t2, t3
				sumX = trees[t1][0] + trees[t2][0] + trees[t3][0]
				sumY = trees[t1][1] + trees[t2][1] + trees[t3][1]
				
				if sumX % 3 == 0 and sumY % 3 == 0:
					result += 1
	
	return result

cases = int(f.readline().strip())
for case in range(cases):
	print "Processing case", case + 1
	v = f.readline().strip().split()
	n = int(v[0])
	a = int(v[1])
	b = int(v[2])
	c = int(v[3])
	d = int(v[4])
	x0 = int(v[5])
	y0 = int(v[6])
	m = int(v[7])
	
	
	trees = []
	x = x0
	y = y0	trees.append((x, y))	for i in range(n - 1):		x = (a * x + b) % m		y = (c * y + d) % m		trees.append((x, y))	
	i = calc(trees);
	print "Result:", i
			
	of.write("Case #" + str(case + 1) + ": " + str(i) + "\n")
