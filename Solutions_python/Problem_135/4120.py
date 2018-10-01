T = input()
for i in range(T):
	g1 = input()
	row1_1 = raw_input().split(" ")
	row2_1 = raw_input().split(" ")
	row3_1 = raw_input().split(" ")
	row4_1 = raw_input().split(" ")
	g2 = input()
	row1_2 = raw_input().split(" ")
	row2_2 = raw_input().split(" ")
	row3_2 = raw_input().split(" ")
	row4_2 = raw_input().split(" ")
	num_count = 0
	is_present = False
	num_common = 0
	if g1 == 1:
		if g2 == 1:
			for a1 in row1_1:
				if a1 in row1_2:
					num_count+=1
					is_present=True
					num_common = a1
		elif g2 == 2:
			for a1 in row1_1:
				if a1 in row2_2:
					num_count+=1
					is_present=True
					num_common = a1
		elif g2 == 3:
			for a1 in row1_1:
				if a1 in row3_2:
					num_count+=1
					is_present=True
					num_common = a1
		elif g2 == 4:
			for a1 in row1_1:
				if a1 in row4_2:
					num_count+=1
					is_present=True
					num_common = a1
	elif g1 == 2:
		if g2 == 1:
			for a1 in row2_1:
				if a1 in row1_2:
					num_count+=1
					is_present=True
					num_common = a1
		elif g2 == 2:
			for a1 in row2_1:
				if a1 in row2_2:
					num_count+=1
					is_present=True
					num_common = a1
		elif g2 == 3:
			for a1 in row2_1:
				if a1 in row3_2:
					num_count+=1
					is_present=True
					num_common = a1
		elif g2 == 4:
			for a1 in row2_1:
				if a1 in row4_2:
					num_count+=1
					is_present=True
					num_common = a1
	elif g1 == 3:
		if g2 == 1:
			for a1 in row3_1:
				if a1 in row1_2:
					num_count+=1
					is_present=True
					num_common = a1
		elif g2 == 2:
			for a1 in row3_1:
				if a1 in row2_2:
					num_count+=1
					is_present=True
					num_common = a1
		elif g2 == 3:
			for a1 in row3_1:
				if a1 in row3_2:
					num_count+=1
					is_present=True
					num_common = a1
		elif g2 == 4:
			for a1 in row3_1:
				if a1 in row4_2:
					num_count+=1
					is_present=True
					num_common = a1
	elif g1 == 4:
		if g2 == 1:
			for a1 in row4_1:
				if a1 in row1_2:
					num_count+=1
					is_present=True
					num_common = a1
		elif g2 == 2:
			for a1 in row4_1:
				if a1 in row2_2:
					num_count+=1
					is_present=True
					num_common = a1
		elif g2 == 3:
			for a1 in row4_1:
				if a1 in row3_2:
					num_count+=1
					is_present=True
					num_common = a1
		elif g2 == 4:
			for a1 in row4_1:
				if a1 in row4_2:
					num_count+=1
					is_present=True
					num_common = a1

	if is_present and num_count < 2:
		print "Case #"+str(i+1)+": "+str(num_common)
	elif is_present and num_count >= 2:
		print "Case #"+str(i+1)+": Bad magician!"
	elif not is_present:
		print "Case #"+str(i+1)+": Volunteer cheated!"
