from sys import argv

script, rname, wname = argv

infile = open(rname)
outfile = open(wname, 'w')

tc = int(infile.readline())

for i in range(1,tc+1):
	y, x = map(int,infile.readline().split(' '))
	ans = 0
	
	# read in the field
	field = []
	for j in range(0,y):
		field.append(map(int, infile.readline().split(' ')))

	#create the field
	newfield = []
	for vert in range (0, y):
		hf = []
		for horiz in range(0,x):
			hf.append(2)
		newfield.append(hf)

	# fields are written [y][x]
	# shave vertical
	shave = True
	for horiz in range(0, x):
		shave = True
		for vert in range(0, y):
			if field[vert][horiz] == 1:
				continue
			else:
				shave = False
				break

		if shave:
			for vert in range(0,y):
				newfield[vert][horiz] = 1

	for vert in range(0, y):
		shave = True
		for horiz in range(0, x):
			if field[vert][horiz] == 1:
				continue
			else:
				shave = False
				break

		if shave:
			for horiz in range(0,x):
				newfield[vert][horiz] = 1

	if newfield != field:
		ans = 1

	s = "YNEOS"
	print("Case #%d: %s" % (i, s[ans::2]))
	outfile.write("Case #%d: %s\n" % (i, s[ans::2]))