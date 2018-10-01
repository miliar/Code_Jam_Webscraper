t = int(raw_input())

for i in range(1, t+1):
	ans1 = int(raw_input())
	b1 = [[int(x) for x in raw_input().split()]for j in range(4)]
	ans2 = int(raw_input())
	b2 = [[int(x) for x in raw_input().split()]for j in range(4)]
	cross = set()
	for x in b1[ans1-1]:
		if x in b2[ans2-1]:
			cross.add(x)
	print "Case #" + str(i) + ":",
	if len(cross) == 0:
		print "Volunteer cheated!"
	elif len(cross) == 1:
		print cross.pop()
	else:
		print "Bad magician!"
