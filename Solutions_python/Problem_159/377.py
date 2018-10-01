for case in range(int(raw_input())):
	raw_input()
	plates = map(int, raw_input().split(' '))
	largest_slope = 0
	comp1_total = 0
	comp2_total = 0
	for i in range(len(plates) - 1):
		if plates[i] > plates[i+1]:
			comp1_total += plates[i] - plates[i+1]
			slope = plates[i] - plates[i+1]
			if slope > largest_slope:
				largest_slope = slope
	for i in range(len(plates) - 1):
		if plates[i] > largest_slope:
			comp2_total += largest_slope
		else:
			comp2_total += plates[i]
	print "Case #%d: %d %d" % (case + 1,comp1_total,comp2_total)
