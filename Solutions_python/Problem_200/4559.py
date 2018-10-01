# import sys

#number = sys.stdin.read()

# def tidy(number):
# number = 1032
# number = 213

# t = int(input())


file = open("B-large.in", "r")
file_contents = file.read()
file_contents_split = file_contents.split("\n")
t = int(file_contents_split[0])

# t = 1
# file_contents_split = [1,789]

# def tidy(number):

for j in range(1, t + 1):
	tidy = False
	number = int(file_contents_split[j])
	string_number = str(number)
	split_string_number = list(string_number)
	split_int_number = [int(element) for element in split_string_number]
	tidy_number = number


	break_index = None

	# print(split_int_number)

	while (tidy == False):
		if len(split_int_number) > 1:
			for i in range(1,len(split_int_number)):
				# print(i)
				if (split_int_number[i] < split_int_number[i-1]):
					# print("here")
					break_index = i
					tidy = False
					break
				else:
					tidy = True
		else:
			tidy = True
			tidy_number = number

		if (tidy == False):
			if (break_index is not None):
				power = len(split_int_number) - break_index
				tidy_number = number - ((number%(10**power)) + 1)
			else:
				tidy_number = number

			number = tidy_number
			string_number = str(number)
			split_string_number = list(string_number)
			split_int_number = [int(element) for element in split_string_number]

	print("Case #{}: {}".format(j, tidy_number))

		# return tidy_number

# tidy(1032)
# tidy(213)
# tidy(132)
# tidy(98)
# tidy(3331)
# tidy(4548)

# tidy(4)
# tidy(132)
# tidy(1000)
# tidy(7)
# tidy(111111111111111110)

