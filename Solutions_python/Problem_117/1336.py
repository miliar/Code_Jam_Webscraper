t = int(raw_input())
for case in xrange(t):
	dim = map(int,raw_input().split())
	lawn = []
	for _ in xrange(dim[0]):
		lawn.append(map(int, raw_input().split()))
	for i, row in enumerate(lawn):
		for j, h in enumerate(row):
			hor, ver = False, False
			for x in row:
				if x>h:
					hor = True
			for i_ in xrange(dim[0]):
				if lawn[i_][j] > h:
					ver = True
			if hor and ver:
				break
		else:
			continue
		break
	else:
		print "Case #" + str(case + 1) + ": YES"
		continue
	print "Case #" + str(case+1) + ": NO"
