def compare(a,b):
	match = 0
	num = 0
	for i in range(4):
		for j in range(4):
			if(a[i]==b[j]):
				match+=1
				num = a[i]
			if(match>=2):
				return "Bad magician!" 
	if(match==1):
		return num
	else:
		return "Volunteer cheated!"

T = int(raw_input())
for t in range(T):
	x = []
	row_x = int(raw_input())
	for i in range(4):
		s = raw_input()
		if(i==row_x-1):
			x = [int(elem) for elem in s.split()]			
		

	y = []
	row_y = int(raw_input())
	for i in range(4):
		s = raw_input()
		if(i==row_y-1):
			y = [int(elem) for elem in s.split()]

	print "Case #" + str(t+1) + ":", compare(x,y)


		
