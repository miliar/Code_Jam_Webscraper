# Crop Triangles

for case in range(input()):
	n, A, B, C, D, x0, y0, M = map(int, raw_input().split())
	X,Y = x0, y0
	co = []
	co.append([X,Y])
	#print X, Y
	for i in range(1,n):
		X = (A * X + B) % M
		Y = (C * Y + D) % M
		co.append([X,Y])
		#print X, Y
	
	c = 0
	for pt1 in range(n):
		for pt2 in range(n):
			for pt3 in range(n):
				if pt1!=pt2 and pt2!=pt3 and pt3!=pt1:
					gX = float(co[pt1][0]+co[pt2][0]+co[pt3][0] ) /3
					gY = float(co[pt1][1]+co[pt2][1]+co[pt3][1] ) /3
					if int(gX)==gX and int(gY)==gY: c+=1
					
	
	print "Case #%s: %s" % (case+1, (c/6))