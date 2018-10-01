data = open("A-large.in","r")
outfile = open("cj_ovation_large_output.txt","w")

t = int(data.readline())

for case in range(0,t):
	current_case = data.readline().split(' ')
	max_shyness = int(current_case[0])
	shyness_values = []
	if '\n' in current_case[1]:
		current_case[1]=current_case[1][:-1]
	for digit in current_case[1]:
		shyness_values.append(int(digit))
	#print shyness_values
	
	shyness_less_than = []
	
	shyness_less_than.append(0)
	shyness_less_than.append(shyness_values[0])
	
	for x in range(2,max_shyness+1):
		shyness_less_than.append(shyness_less_than[x-1]+shyness_values[x-1])
	
	#print "\n"
	
	#print shyness_less_than
	
	for x in range(0,len(shyness_less_than)):
		shyness_less_than[x] = x - shyness_less_than[x]
		
	#print shyness_less_than
	
	outfile.write("Case #" + str(case+1) + ": " + str(max(max(shyness_less_than),0)))
	if case < t-1: outfile.write("\n")