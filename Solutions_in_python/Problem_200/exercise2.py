def is_tidy(numbers):
	for i in xrange(len(numbers) - 1, 0, -1):
		if (long(numbers[i]) < long(numbers[i - 1])):
			return False
	return True

def get_tidy(numbers):
	if (is_tidy(numbers)):
		return numbers
	for i in xrange(len(numbers) - 1, 0, -1):
		if (numbers[i] < numbers[i-1]):
			if (numbers[i] == "0"):
				temp = int(''.join(numbers)) - 1*(10**(len(numbers) - 1 - i))
				numbers = list(str(temp))
				for j in xrange(len(numbers) - 1, i-1, -1):
					numbers[j]   = str(9)
			else:
				numbers[i-1] = str(int(numbers[i-1]) - 1)
				for j in xrange(len(numbers) - 1, i-1, -1):
					numbers[j]   = str(9)
	return get_tidy(numbers)

count = 0
number_of_cases = 0
file_object = open("ex2.txt", "r")
for line in file_object:
	if (count == 0):
		count += 1
		number_of_cases = int(line)
		continue
	number = int(line.replace("\n", "").replace(" ",""))
	last_tidy_number = 0
	numbers = list(str(number))		
	numbers = get_tidy(numbers)
	last_tidy_number = int(''.join(numbers))
	print("Case #{}: {}".format(count, last_tidy_number))
	count += 1