def counting(somels, someinfo):
	counter = 0
	if (len(somels) == 0):
		return counter
	else:
		for k in somels:
			if ((k[0]-someinfo[0])*(k[1]-someinfo[1]) < 0):
				counter = counter+1
	return counter



myin = open("A.in")
myout = open("A1C.out","w")
inputnum = int(myin.readline().strip())
for k in range(1,inputnum+1):
	floor = int(myin.readline().strip())
	intersect = 0
	thelis = set([])
	for t in range(floor):
		peop = myin.readline().strip().split()
		info = (int(peop[0]),int(peop[1]))
		intersect = intersect+counting(thelis,info)
		thelis.add(info)
	myout.write("Case #")
	myout.write(str(k))
	myout.write(": ")
	myout.write(str(intersect))
	myout.write("\n")