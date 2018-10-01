import sys
inp = open(sys.argv[1],"r")
outp = open(sys.argv[2],"w")
case_count = int(inp.readline())

for case_num in range(1,case_count+1):
	table = []
	for i in range(4):
		row = inp.readline().strip()
		assert(len(row)==4)
		table.append(row)
	assert(len(inp.readline().strip())==0)


	# determine who had just moved
	x_count = 0
	o_count = 0
	empty_count = 0
	for i in range(4):
		for j in range(4):
			if table[i][j]=="X":
				x_count += 1
			elif table[i][j]=="O":
				o_count += 1
			elif table[i][j]==".":
				empty_count += 1
			else:
				assert table[i][j] == "T"

	if x_count>o_count:
		assert(x_count==o_count+1)
		player = "X"
	else:
		assert(x_count==o_count)
		player = "O"

	# did she won?
	won = False

	# in rows?

	for i in range(4):
		all_of_it = True
		for j in range(4):
			all_of_it = all_of_it and (table[i][j] in [player,"T"])
		if all_of_it:
			won = True
			break

	# in colls?

	if not won:
		for j in range(4):
			all_of_it = True
			for i in range(4):
				all_of_it = all_of_it and (table[i][j] in [player,"T"])
			if all_of_it:
				won = True
				break


	# in +diagonal?

	if not won:
		all_of_it = True
		for i in range(4):
			j = i
			all_of_it = all_of_it and (table[i][j] in [player,"T"])
		won = all_of_it


	# in -diagonal?

	if not won:
		all_of_it = True
		for i in range(4):
			j = 3-i
			all_of_it = all_of_it and (table[i][j] in [player,"T"])
		won = all_of_it


	# so won?

	if won:
		outp.write("Case #%i: %s won\n"%(case_num,player))
	else:
		if empty_count==0:
			outp.write("Case #%i: Draw\n"%(case_num,))	
		else:
			outp.write("Case #%i: Game has not completed\n"%(case_num,))