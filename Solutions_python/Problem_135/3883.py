t = int(raw_input())
case = 1
while (case <= t):
	a1 = int(raw_input()) - 1
	arr1 = [None] * 4
	for i in range(0, 4):
		arr1[i] = raw_input().split(" ")
	
	a2 = int(raw_input()) - 1
	arr2 = [None] * 4
	for i in range(0, 4):
		arr2[i] = raw_input().split(" ")

	answer = -1
	c = 0
	for i in range(0, 4):
		a = arr1[a1][i]
		for j in range(0, 4):
			if a == arr2[a2][j]:
				c += 1
				answer = arr2[a2][j]

	if c == 0:
		print "Case #%d: Volunteer cheated!" % case

	elif c == 1:
		print "Case #%d: %s" % (case, answer)

	else:
		print "Case #%d: Bad magician!" % (case)

	case += 1