def displayArray(my_array):
	for i in range(len(my_array)):
		print i

for tc in range(1, int(raw_input())+1):
	y = ''

	X, R, C= map(int, raw_input().split())

	if R * C % X == 0:
		if X == 1:
			y = 'GABRIEL'
		elif X ==2:
			y = 'GABRIEL'
		elif X == 3:
			if min(R,C) == 1:
				y = 'RICHARD'
			else:
				y = 'GABRIEL'
		elif X ==4:
			if min(R,C) == 1 or min(R,C) == 2:
				y = 'RICHARD'
			else:
				y = 'GABRIEL'

	else:
		y = 'RICHARD'




	#if y != ''
	print "Case #{}: ".format(tc) + str(y)
	#else:
	#print "Case #{}".format(tc) + stry(y)
		
	
