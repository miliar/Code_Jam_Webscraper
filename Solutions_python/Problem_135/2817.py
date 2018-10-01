import sys

oF = open(sys.argv[1])

T = int(oF.readline().strip())

for i in range(T):
	

	row1 = int(oF.readline().strip())
	for j in range(4):
		if j+1 == row1:
			A = set([int(a) for a in oF.readline().strip().split()])
		else:
			oF.readline()

	row2 = int(oF.readline().strip())
	for j in range(4):
		if j+1 == row2:
			B = set([int(a) for a in oF.readline().strip().split()])
		else:
			oF.readline()

	C = A & B
	if len(C) == 0:
		print("Case #%d: Volunteer cheated!"%(i+1))
	elif len(C) == 1:
		print ("Case #%d: %d"%(i+1,list(C)[0]))
	else:
		print ("Case #%d: Bad magician!"%(i+1))
