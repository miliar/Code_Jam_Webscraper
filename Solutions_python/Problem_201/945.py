# Google Code Jam practice problems

#file_in = "test.txt"
#file_in = "C-small-1-attempt0.in"
#file_in = "C-small-2-attempt2.in"
file_in = "C-large.in"

#file_in = "c2.in"

file_out = "output_large.txt"

def answer(test_case):
	test_case = test_case.split()
	num_stalls = int(test_case[0])
	num_users = int(test_case[1])
	
	print(num_stalls, "stalls", "and", num_users, "users")
	if num_users == 1:
		final = split_stalls(num_stalls)
	str_bin = str(bin(num_users))[3:]
	#print("str_bin", str_bin)
	for i in range(len(str_bin)-1, -1, -1):
		print(str_bin[i])
		stall_choices = split_stalls(num_stalls)
		print("stall choices", stall_choices)
		#print(digit)
		if str_bin[i] == "0":
			num_stalls = stall_choices[0]
		elif str_bin[i] == "1":
			num_stalls = stall_choices[1]
		else:
			print("theres a bug")
	final = split_stalls(num_stalls)
	print(final)
	return final
		
def split_stalls(n):
	if n == 0:
		return [0,0]
		
	if n % 2 == 0:
		return [n//2, n//2 - 1]
	else:
		return [n//2, n//2]
		
def add_user(stalls):
	max = (0,0)
	for i in range(len(stalls)):
		if stalls[i] > max[0]:
			max = (stalls[i], i)
	num = stalls.pop(max[1])
	if num % 2 == 0:
		left_num = num//2 - 1
		right_num = num//2
	else:
		left_num = num//2
		right_num = num//2
	stalls.insert(max[1], right_num)
	stalls.insert(max[1], left_num)
		
	return stalls
	
def write_file():
	f = open(file_in)
	out = open(file_out, "w")
	num_cases = int(f.readline())
	for i in range(num_cases):
	#for i in range(3):
		test_case = f.readline().strip()
		output = answer(test_case)
		out.write("Case #" + str(i+1) + ": " + str(output[0]) + " " + str(output[1]) + "\n")
		print("Case #" + str(i+1) + ": " + str(output))
		print()
	f.close()
	out.close()
	#compare_outputs()
	
write_file()