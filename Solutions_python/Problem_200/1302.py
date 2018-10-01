from datetime import datetime
import math

input_file_path = 'B-large.in.txt'


def digits_to_num(digits):
	num = 0
	for i in range(1,len(digits)+1):
		num = num + digits[-i] * pow(10,i-1)
	return num


def find_tidy_num(n):		# n is a string here
	if len(n) == 1:
		return n
	digits = [int(d) for d in n]
	i=1
	done = False
	while(not done):
		if i<len(digits) and digits[i] >= digits[i-1]:
			i = i+1
		else:
			done = True
	if i >= len(digits):
		return str(digits_to_num(digits))
	else:
		to_subtract = digits_to_num(digits[i:])+1
		n_modified = str(long(n) - to_subtract)
		return find_tidy_num(n_modified)



start = datetime.now()

with open(input_file_path) as f:
	lines = f.read().splitlines()
	for j in range(1,int(lines[0])+1):
		n = lines[j]
		out = find_tidy_num(n)
		print 'Case #' + str(j) + ': ' + out


diff = datetime.now() - start
#print diff