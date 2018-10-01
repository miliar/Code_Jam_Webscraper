for i in range(input()):
	x,y=map(int,raw_input().split())
	z=0
	for j in range(40):
		if x<=j*j and j*j<=y and str(j)==str(j)[::-1] and str(j*j)==str(j*j)[::-1]:
			z+=1
	print "Case #%d: %d"%(i+1,z)
