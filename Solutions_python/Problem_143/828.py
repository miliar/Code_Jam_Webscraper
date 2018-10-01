input_file = open('/Users/Aida/Desktop/googlecodejam/input_round1a.txt')
output_file = open('/Users/Aida/Desktop/googlecodejam/output_round1a.txt', 'w')

N = int(input_file.readline()) # number of test cases
A =[] # old
B = [] # new
K = [] # cat

i =1

while i <= N:
	count = 0
	new_case = input_file.readline().split()

	#print new_case

	A = range(int(new_case[0]))
	B = range(int(new_case[1]))
	K = range(int(new_case[2]))

	for num in A:
		for entry in B:
			if num & entry in K:
				count +=1

	output_file.write("Case #" + str(i) + ": " + str(count))

	i +=1
	if i<= N:
		output_file.write("\n")

input_file.close()
output_file.close()