import collections
f = open('magic.in', "r")
lines = f.readlines()
f.close()

cases = int(lines[0])


current_case=0

while current_case < cases:
	first_answer = int(lines[current_case*10+1])
	second_answer = int(lines[current_case*10+6])
	first_line = lines[current_case*10+1+first_answer].replace('\n','')
	second_line =lines[current_case*10+6+ second_answer].replace('\n','') 	
        f1 = [int(i) for i in first_line.split()]
	f2 = [int(i) for i in second_line.split()]
	results_list = f1+f2
	solution = [x for x, y in collections.Counter(results_list).items() if y > 1]
        if len(solution) == 0:
		print 'Case #{0}: Volunteer cheated!'.format(current_case+1)	
        if len(solution) ==1:
		print 'Case #{0}: {1}'.format(current_case+1,solution[0])
	if len(solution) >1:
		print 'Case #{0}: Bad magician!'.format(current_case+1)

	current_case+=1
	
	
	 
