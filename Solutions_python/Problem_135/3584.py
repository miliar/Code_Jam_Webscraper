f = open('a.in', 'r')
out = open('a.out', 'w')
a = f.readline()
for cases in range(int(a)):
	c=range(4)
	d=range(4)
	first = f.readline()
	for c1 in range(4):
		aa=f.readline()
		if c1 == int(first)-1:
			temp = aa.split(" ")
			for cc in range(4):
				c[cc] = int(temp[cc])
	second = f.readline()
	for c2 in range(4):
		aa=f.readline()
		if c2 == int(second)-1:
			temp = aa.split(" ")
			for cc in range(4):
				d[cc] = int(temp[cc])
	print c
	print d
	if (c[0] == d[0] or c[0] == d[1] or c[0] == d[2] or c[0] == d[3]) + (c[1] == d[0] or c[1] == d[1] or c[1] == d[2] or c[1] == d[3]) + (c[2] == d[0] or c[2] == d[1] or c[2] == d[2] or c[2] == d[3]) + (c[3] == d[0] or c[3] == d[1] or c[3] == d[2] or c[3] == d[3]) > 1 :
		print "Case #" + str(cases+1) + ": Bad magician!"
		out.write("Case #" + str(cases+1) + ": Bad magician!" + "\n")
	elif c[0] == d[0] or c[0] == d[1] or c[0] == d[2] or c[0] == d[3]:
		print "Case #" + str(cases+1) + ": " + str(c[0])
		out.write("Case #" + str(cases+1) + ": " + str(c[0]) + "\n")
	elif c[1] == d[0] or c[1] == d[1] or c[1] == d[2] or c[1] == d[3]:
		print "Case #" + str(cases+1) + ": " + str(c[1])
		out.write("Case #" + str(cases+1) + ": " + str(c[1]) + "\n")
	elif c[2] == d[0] or c[2] == d[1] or c[2] == d[2] or c[2] == d[3]:
		print "Case #" + str(cases+1) + ": " + str(c[2])
		out.write("Case #" + str(cases+1) + ": " + str(c[2]) + "\n")
	elif c[3] == d[0] or c[3] == d[1] or c[3] == d[2] or c[3] == d[3]:
		print "Case #" + str(cases+1) + ": " + str(c[3])
		out.write("Case #" + str(cases+1) + ": " + str(c[3]) + "\n")
	else:
		print "Case #" + str(cases) + ": Volunteer cheated!"
		out.write("Case #" + str(cases+1) + ": Volunteer cheated!" + "\n")