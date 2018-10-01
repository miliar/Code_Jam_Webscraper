def read_file():
	f = open('c:\Python33\A-small-attempt0.in', 'r')
	num_case = int(f.readline())
	
	for n in range(num_case):
		rowA_input = int(f.readline())
		for i in range(4):
			line_input = f.readline()
			if(i==rowA_input-1):
				listA_input = line_input.split()
			
		rowB_input = int(f.readline())
		for j in range(4):
			line_input = f.readline()
			if(j==rowB_input-1):
				listB_input = line_input.split()
		
		print_result(n+1, listA_input, listB_input)

def print_result(case, listA, listB):
	result = compare(listA,listB)
	if(result[0] == 1):
		print('Case #{}: {}'.format(case, result[1]))
	elif(result[0] > 1):
		print('Case #{}: Bad magician!'.format(case))
	elif(result[0] == 0):
		print('Case #{}: Volunteer cheated!'.format(case))
		
def compare(listA, listB):
	counter = 0
	card = 0
	for i in listA:
		for j in listB:
			if(int(i)==int(j)):
				counter+=1
				card = i
				
	return [counter,card]
		
read_file()