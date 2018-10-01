T = int(raw_input())

for tt in range(T):
	a1 = int(raw_input())
	A = []
	for ii in range(4):
		A.append(set(map(int, raw_input().split(" "))))
	a2 = int(raw_input())
	B = []
	for ii in range(4):
		B.append(set(map(int, raw_input().split(" "))))
	if len(A[a1-1].intersection(B[a2-1])) == 1:
		msg = str(list(A[a1-1].intersection(B[a2-1]))[0])
	if len(A[a1-1].intersection(B[a2-1])) > 1:
		msg = "Bad magician!"
	if len(A[a1-1].intersection(B[a2-1])) < 1:
		msg = "Volunteer cheated!"
	print "Case #{0}: {1}".format(str(tt+1), msg)
