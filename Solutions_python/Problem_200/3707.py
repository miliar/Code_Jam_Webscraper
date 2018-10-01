import math

#returns -1 if is tidy; or position (starting with farthest to R as 1) of first untidy num
def find_first_untidy(x):
	counter = 1
	while(x >= 10):
		last_digit = x % 10
		x = x/10
		second_to_last_digit = x % 10
		if (last_digit < second_to_last_digit):
			return counter
		else:
			counter += 1
	return -1

def process_untidy(n, first_untidy):
	while (first_untidy != -1):
		# Replace n with "tidier" n one number at a time
		# cut off end of number starting at first untidy part
		#print "n is %d" % n
		#print "first_untidy is %d" % first_untidy
		mod_num = pow(10, first_untidy + 1)
		#print "mod_num is %d" % mod_num
		untidy_end = n % mod_num
		#print "untidy end is %d" % untidy_end
		start_of_number = (n / mod_num) * mod_num
		#print "strt of number is %d" % start_of_number
		untidy_end_str = str(untidy_end)
		first_digit_str = untidy_end_str[0]
		first_digit = int(first_digit_str)
		#print "first digit is %d" % first_digit
		first_digit -= 1
		first_digit = (first_digit * 10) + 9
		#print "first digit is now (should be two digits) %d" % first_digit
		first_digit_str = str(first_digit)
		for i in range(0, first_untidy - 1):
			first_digit_str = first_digit_str + '9'
		first_digit = int(first_digit_str)
		#print "tidied part of that number is now %d" % first_digit
		n = start_of_number + first_digit
		#print "n is now %d" % n
		# keep going until you find no more untidy parts
		first_untidy = find_first_untidy(n)
	return n


def determine_largest_tidy(n):
	if (n > 10):
		tidy_num = find_first_untidy(n)
		if (tidy_num == -1):
			return n
		else:
			return process_untidy(n, tidy_num)	 
	else:
		return n

#main program

input_file = open("B-large.in.txt", "r")
output_file = open("large_output.txt", "w+")

# get t
t = int(input_file.readline())

# get first n, which we know is >= 1
next = input_file.readline()
counter = 1
while next:
	n = int(next)
	tidy = determine_largest_tidy(n)
	output_file.write("Case #%d: %d" % (counter, tidy))
	if counter < t:
		output_file.write("\n")
	counter += 1
	next = input_file.readline()

input_file.close()
output_file.close()