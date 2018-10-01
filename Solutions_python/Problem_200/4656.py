def problem():

	t = input()

	file1 = open("smallOuput.txt","w+")

	def solution(n,h):
		numbers = n
		if n<=9:
			if h!=t-1:
				file1.write("Case #"+str(h+1)+": "+str(n)+"\n")
			else:
				file1.write("Case #"+str(h+1)+": "+str(n))
			# file1.write("Case #"+str(h+1)+": "+str(n)+"\n")
			return 
		string = ""	
		while numbers>=1:
			boolean_increasing = True
			dummy = numbers
			while dummy > 0:
				d1 = dummy % 10;
				dummy = dummy/10;
				d2 = dummy % 10;
				# print d1,d2
				if d2>d1:
					# print numbers,d2,d1
					boolean_increasing = False
					break
			if boolean_increasing==True:
				# file1.write(numbers)
				if h!=t-1:
					file1.write("Case #"+str(h+1)+": "+str(numbers)+"\n")
				else:
					file1.write("Case #"+str(h+1)+": "+str(numbers))
				# print numbers
				break
			numbers-=1
	


	# with open("smallInput.txt","r") as inp:
	# 	for line in inp:
	# 		line = line.strip()
	# 		if len(line)==1:
				
	

	for h in xrange(t):
		n = input()
		# print n
		if n<=1000:
			solution(n,h)
	file1.close()
	file1 = open("smallOuput.txt","r")
	# print file1.read()
	for line in file1:
		print line,


problem()
# print 111111111111111110-99999999999999999