import sys

NUMBER_OF_ROWS = 4

def main(input_file):
	number_of_cases = int(input_file.readline().strip("\n"))
	for case_number in xrange(1, number_of_cases + 1):
		print "Case #%d: %s" % (case_number, case(input_file))

def case(input_file):
	set1 = sub_case(input_file)
	set2 = sub_case(input_file)
	interset = set1.intersection(set2)
	intersection_length = len(interset)
	if intersection_length == 0:
		return "Volunteer cheated!"
	elif intersection_length > 1:
		return "Bad magician!"
	else:
		return "%d" % (interset.pop(), )

def sub_case(input_file):
	row_number = int(input_file.readline().strip("\n"))
	for i in xrange(row_number - 1):
		input_file.readline()
	sub_case_set = set([int(card_number) for card_number in input_file.readline().strip("\n").split(" ")])
	for i in xrange(NUMBER_OF_ROWS - row_number):
		input_file.readline()
	return sub_case_set

if __name__ == '__main__':
	main(open(sys.argv[1]))


