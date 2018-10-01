def execute():
	filename = 'C-small-attempt0.in'
	fp = open(filename,"r")
	noc = int(fp.readline())
	num = 0
	caseno = 1
	for x in range(noc):
		A,B=fp.readline().strip().split()
		A = int(A)
		B = int(B)
		if A/10 is 0:
			num = 0
		else:
			all_numbers=[]
			for i in xrange(A,B+1):
				x = map(int, str(i)) 
				numbers=[]
				index = 0
				end = len(x)
				numbers.append(int(''.join(str(i) for i in x[0:end])))
				for j in xrange(len(x)-1):	
					end = end - 1
					index = index - 1
					num = int(''.join(str(i) for i in x[index:]+x[0:end]))
					if((num >= A) and (num <=B)):
						numbers.append(num)
				numbers.sort()
				if(numbers[1:]!=numbers[:-1]):
					numbers = [numbers[i] for i in range(len(numbers)) if i == 0 or numbers[i] != numbers[i-1]]
					if((len(numbers) > 1)):
						all_numbers.append(numbers)		
			all_numbers.sort()
			all_numbers = [all_numbers[i] for i in range(len(all_numbers)) if i == 0 or all_numbers[i] != all_numbers[i-1]]
			#print all_numbers	
			num = len(all_numbers)
			for i in all_numbers:
				if len(i) is 3:
					num = num + 2
				if len(i) is 4:
					num = num + 5
				if len(i) is 5:
					num = num + 9
					
		print "Case #%d: %d"%(caseno,num)
		caseno = caseno + 1
if __name__=='__main__':
	execute()