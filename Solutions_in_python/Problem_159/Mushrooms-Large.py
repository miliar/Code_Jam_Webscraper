

def method1(l):
	min_mushrooms = 0
	for i in range(1,len(l)):
		if l[i-1] - l[i] > 0:
			min_mushrooms += l[i-1] - l[i]
	
	return min_mushrooms

def method2(l):
	min_mushrooms = 0
	eat_rate = max_between_values(l)
	for i in range(len(l)-1):
		eat_iter = 0
		if l[i] >= eat_rate:
			eat_iter = eat_rate
		else:
			eat_iter = l[i]
		min_mushrooms += eat_iter
	
	return min_mushrooms

def max_between_values(l):
	max = -1
	for i in range(len(l)-1):
		if l[i] - l[i+1] > max:
			max = l[i] - l[i+1]		
	
	return max

def solveMushrooms():
	input = open("A-large.in", "r")
	output = open("A-large-output-Mushrooms", "w")

	test_cases = int(input.readline().strip("\n"))
	tc = 1


	for i in range(test_cases):
		iter = map(int, input.readline().strip("\n"))
		li = map(int, input.readline().strip("\n").split(" "))
		
		y = method1(li)
		z = method2(li)

		output.write("Case #{0}: {1} {2}\n".format(tc, y, z))
		tc += 1

	input.close()
	output.close()
