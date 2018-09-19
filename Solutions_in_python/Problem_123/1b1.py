def file_read(file):
	file_open = open(file, 'r')
	
	for line in file_open:
		yield line
	
	file_open.close()

input = file_read('A-large.in')
output = open("A-large.out","w")

T = int(input.next())

for i in xrange(T):
	line1 = input.next().split()

	A = int(line1[0])
	N = line1[1]

	motes = [int(j) for j in input.next().split()]

	motes.sort()
	
	solutions = []
	for j in xrange(len(motes)):
		count = 0
		remaining = len(motes) - j - 1
		if A == 1:
			for k in xrange(len(motes)):
				solutions += [1]
			break
		
		while A <= motes[j]:
			count += 1
			A += A - 1
		
		A = A + motes[j]
		
		if count == 0:
			solutions += [0]
		elif count <= remaining:
			solutions += [count]
		elif count > remaining:
			for k in xrange(remaining+1):
				solutions += [1]
			for k in xrange(len(solutions)-1, -1, -1):
				if solutions[k] > 0:
					solutions[k] = 1
				else:
					break
			break
	
	answer = sum(solutions)
	
	output.write("Case #"+str(i+1)+": "+str(answer)+"\n")
	