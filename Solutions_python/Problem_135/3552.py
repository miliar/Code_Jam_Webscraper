#!/bin/python

t = input()
i = 1
while i <= t:
	grid1 = []
	grid2 = []
	row_i = input()
	some = 0
	while some < 4:
		grid1.append(raw_input().split(" "))
		some += 1


	row_j = input()
	some = 0
	while some < 4:
		grid2.append(raw_input().split(" "))
		some += 1

	a, b = set(grid1[row_i - 1]), set(grid2[row_j - 1])
	c = a & b

	if len(c) == 1:
		print "Case #%d: %s" % (i, c.pop())
	elif len(c) > 1:
		print "Case #%d: Bad magician!" % (i,)
	elif len(c) == 0:
		print "Case #%d: Volunteer cheated!" % (i,)

	i += 1