t = int(raw_input())

winner = []
for i in range(t):
	x, r, c = raw_input().split()

	x = int(x)
	r = int(r)
	c = int(c)
	a = r*c
	if (x == 1):
		winner.append("GABRIEL")
	elif (x==2):
		if (a%2==0):
			winner.append("GABRIEL")
		else:
			winner.append("RICHARD")
	elif (x==3):
		if (a%3==0 and a > 3):
			winner.append("GABRIEL")
		else:
			winner.append("RICHARD")
	elif(x==4):
		if(a%4==0 and a > 8):
			winner.append("GABRIEL")
		else:
			winner.append("RICHARD")

for i in range(t):
	print "Case #%d: %s" %((i+1), winner[i])