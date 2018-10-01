import sys, os, copy

# predefine the tidy numbers so that you only have to search after the last predefined tidy
# N <= to 10^18
tidy_nums = [9, 99, 999, 9999, 99999, 999999, 9999999, 99999999, 999999999, 9999999999, 99999999999, 999999999999, 9999999999999, 99999999999999, 999999999999999, 9999999999999999, 99999999999999999, 999999999999999999]
def generateTidyNums(max_n):
	nine = '9'
	times = 1
	while int(times*nine) < max_n:
		tidy_nums.append(int(times*nine))
		times += 1
# generateTidyNums(10**18)


def isTidy(num):
	max_so_far = 0
	s = str(num)
	for char in s:
		if int(char) < max_so_far:
			return False
		else:
			max_so_far = int(char)
	return True

def findGreatestTidyLessThanN(tidy_nums, n):
	greatest_tidy = 1
	for tidy in tidy_nums:
		if tidy > n: 
			return greatest_tidy
		else:
			greatest_tidy = tidy



def solve(n):
	last_tidy = findGreatestTidyLessThanN(tidy_nums, n)
	for i in reversed(range(last_tidy, n+1)):
		print(i)
		if isTidy(i):
			return str(i)
	return str(last_tidy)






with open(sys.argv[1], 'r') as input_file:
	with open(sys.argv[2], 'w') as output_file:
		t = int(input_file.readline())
		print(t)
		for i in range(t):
			problem = input_file.readline().strip()
			n = int(problem)
			print('N: ', n)
			solution = solve(n)
			print("Case #"+str(i+1)+": "+solution)

			output_file.write("Case #"+str(i+1)+": "+solution+'\n')