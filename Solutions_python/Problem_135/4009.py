f = open('A-small-attempt1.in', 'r')
fo = open('output.txt','w')

numcases = f.readline().strip('\n')
numcases = int(numcases)

for i in range(0,numcases):
	line1 = []
	line2 = []
	rownum1 = f.readline().strip('\n')
	rownum1 = int(rownum1)
	for j in range(0,4):
		row = f.readline().strip('\n')
		if rownum1-1 == j:
			line1 = row.split(' ')
	
	rownum1 = f.readline().strip('\n')
	rownum1 = int(rownum1)
	for j in range(0,4):
		row = f.readline().strip('\n')
		if rownum1-1 == j:
			line2 = row.split(' ')
			
	candidates = []
	for j in range(0,4):
		for k in range(0,4):
			if line1[k] == line2[j] and line2[j] not in candidates:
				candidates.append(line2[j])
				
	fo.write("Case #" + str(i + 1) + ": ")
	if len(candidates) == 0:
		fo.write("Volunteer cheated!\n")
	elif len(candidates) == 1:
		fo.write(str(candidates[0]) + "\n")
	else:
		fo.write("Bad magician!\n")
	
	
	
	
	
	
	
	
	
f.close()
fo.close()