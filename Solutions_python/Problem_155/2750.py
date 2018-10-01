
fin = open('A-large.in', 'r')
fout = open('output.txt', 'w')
index = 1

line = fin.readline() # first line skip




line = fin.readline()

while line:
	# initialize
	list = line.split()
	s_max = int(list[0])
	s_string = list[1]
	friends = 0
	sum = 0

	# do something
	for i in range(0, s_max+1):
		si = int(s_string[i])
		if i==0:
			sum += si
		elif sum < i:
			for k in range(0, i-sum):
				friends += 1
				sum += 1
			sum += si
		else:
			sum += si

	print 'smax %d, friends %d' % (s_max, friends)
	
	fout.write('Case #%d: %d\n' %(index, friends))

	index += 1
	sum = 0
	line = fin.readline()

fin.close()
fout.close()



