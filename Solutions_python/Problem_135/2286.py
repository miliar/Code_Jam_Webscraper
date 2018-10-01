import sys

input_list = []
output_list = []

def get_result(input_list):
	B = 'Bad magician!'
	C = 'Volunteer cheated!'
	return_list = []
	for x in input_list[0]:
		if x in input_list[1]:
			return_list.append(x)
		else:
			pass
	if len(return_list) == 0:
		return C
	elif len(return_list) == 1:
		return return_list[0]
	else:
		return B

try:
	input_filename = sys.argv[1]
	output_filename = input_filename[:sys.argv[1].find('.')]+'.out'
except:
	print 'input filename as argv'
	exit()

try:
	input_f = open("./"+input_filename)
	input_lines = input_f.readlines()
	input_lines2 = []
	input_lines2_count = 0
	i = 0
	j = 0
	for i in range(1, len(input_lines)):
		input_line = input_lines[i]
		input_line_split = input_line.split()
		input_line_split_int = map(int, input_line_split)
		#print 'ok 1'
		j += 1
		if j == 1:
			#print input_lines2
			#print input_lines2_count
			#print input_line_split_int
			input_lines2.append([input_line_split_int])
			#print 'ok 2'
		elif j < 10:
			input_lines2[len(input_lines2)-1].append(input_line_split_int)
			#print 'ok 3'
		else:
			input_lines2[len(input_lines2)-1].append(input_line_split_int)
#			input_lines2_count += 1
			j = 0
			#print 'ok 4'
	input_f.close()
	
	#print input_lines2

	for x in input_lines2:
		#print 'next'
		#print x
		A = x[0][0]
		B = x[5][0]+5
		#print A, B
		#print len(x)
		input_list.append([x[A], x[B]])
	
except:
	print 'read error'
	exit()

#input_list.pop(0)

for x in input_list:
	# do some works here
#	print input_list
	result = get_result(x)
	output_list.append([result])
	print

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
