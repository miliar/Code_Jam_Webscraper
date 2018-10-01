def gabeWins(t):
	print "Case #"+str(t+1)+": GABRIEL"

def richardWins(t):
	print "Case #"+str(t+1)+": RICHARD"

for t in range(input()):
	X, R, C = map(int, raw_input().split())
	if X == 1:
			gabeWins(t)
	elif X == 2:
		if R*C % 2 == 0:
			gabeWins(t)
		else:
			richardWins(t)
	elif X == 3:
		if R*C in [6,9,12]:
			gabeWins(t)
		else:
			richardWins(t)
	elif X == 4:
		if R*C in [12, 16]:
			gabeWins(t)
		else:
			richardWins(t)