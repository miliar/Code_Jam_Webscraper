def  fairsquare(input):
	file = open(input, 'r')
	output = open(input[:-2]+'out', 'w')
	T = int(file.readline())
	for k in range(T):
		line = file.readline().strip('\n').split(' ')
		A = int(line[0])
		B = int(line[1])
		valids = 0
		for i in range(1, B+1):
			if i*i >= A and i*i <= B and str(i) == str(i)[::-1] and str(i*i) == str(i*i)[::-1]:
				valids += 1
		output.write('Case #%d: %d\n' %(k+1, valids))
		
		
fairsquare('C-small-attempt0.in')