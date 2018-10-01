class horse:
	dist=[]
	speed=[]
n = int(input())
for i in range (1, n+1):
	lister=[]
	speeder=[]
	line1 =input().split()
	for j in range (0, int(line1[1])):
		h=horse()
		foo=input().split()
		h.dist=int(foo[0])
		h.speed=int(foo[1])
		lister.append(h)
	for j in range (0, len(lister)):
		remdist = int(line1[0])-lister[j].dist
		spe=lister[j].speed
		speeder.append(float(remdist/spe))
	maxx = max(speeder)
	printer = float(int(line1[0])/maxx)
	print ("Case #"+str(i)+":", end=' ')
	print ("%.6f" %printer)