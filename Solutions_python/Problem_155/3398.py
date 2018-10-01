import sys

input_list = []
output_list = []

def sum_new(list_str):
	result = 0
	for x in list_str:
		x_int = int(x)
		result = result + x_int
	return result

def work(input_line):
	print input_line
	result_max = 0
	for x in range(input_line[0]+1):
		y = int(input_line[1][x])
		if x == 0:
			if y == 0:
				result_max = 1
			else:
				result_max = 0
		else:
			result_temp = x-sum_new(input_line[1][0:x])
			if result_temp > result_max:
				result_max = result_temp
	return result_max

try:
	input_filename = sys.argv[1]
	output_filename = input_filename[:sys.argv[1].find('.')]+'.out'
except:
	print 'input filename as argv'
	exit()

try:
	input_f = open("./"+input_filename)
	input_lines = input_f.readlines()
	input_line_list = []
	for input_line in input_lines:
		input_split = input_line.split()
		input_split[0] = int(input_split[0])
		input_list.append(input_split)
	input_f.close()
except:
	print 'read error'
	exit()
print input_list

input_list.pop(0)

for input_line in input_list:

	# do some works here
	result = work(input_line)
	output_list.append([result])

try:
	output_f = open("./"+output_filename, "w")
	output_f.close()
except:
	pass

try:
	output_f = open("./"+output_filename, "a")
	output_str = ''

	for x in range(len(output_list)):
		output_f.write('Case #' + str(x+1)+': '+str(output_list[x][0])+"\n")
		print x
	output_f.close()
except:
	print 'write error'
	exit()
