infile = open("input.txt", "r")
outfile = open("output.txt", "w")

ncases = int(infile.readline())
for case in xrange(ncases):
	lawn = []
	sizestr = infile.readline().split()
	rows = int(sizestr[0])
	cols = int(sizestr[1])
	for row in xrange(rows):
		line = infile.readline()
		lawn.append([int(i) for i in line.split()])

	possible = True
	for y in xrange(0, rows):
		for x in xrange(0, cols):
			height = lawn[y][x]
			rbigger = [j>height for j in lawn[y]]
			cbigger = [lawn[j][x]>height for j in xrange(0, rows)]
			rtruths = [t for t in rbigger if t]
			ctruths = [t for t in cbigger if t]

			if len(rtruths)>0 and len(ctruths)>0:
				possible = False
	if possible:
		print >>outfile, "Case #%d: YES" % (case+1)
	else:
		print >>outfile, "Case #%d: NO" % (case+1)

infile.close()
outfile.close()