from __future__ import division

__author__ = "huynh.trung.anh@gmail.com (Anh Huynh)"

def read(file_name):
	"""
		Read input file
		Args:
			file_name: str
		Returns:

	"""
	fi = open(file_name, "rb")
	number_test_cases = int(fi.readline())

	case_dict = read_case(fi, number_test_cases)

	fi.close()
	return (number_test_cases, case_dict)

def read_case(fi, number_test_cases):
	"""
		Read relevant data for each case,
		depending on the problem
	"""
	case_dict = {}
	# make changes here

	for case in xrange(number_test_cases):
		case_dict[case] = []
		number_of_blocks = int(fi.readline())
		Naomi_blocks = sorted(map(float, fi.readline().split(" ")))
		Ken_blocks = sorted(map(float, fi.readline().split(" ")))
		case_dict[case] = [number_of_blocks, Naomi_blocks, Ken_blocks]

	return case_dict

def write(file_name, number_test_cases, answer):
	"""
		Write output file
		Args:
			file_name: str
		Returns:

	"""
	# make changes here

	fo = open(file_name, "wb")
	for i in range(number_test_cases):
		fo.write("Case #%d: %d %d\n" % (i+1, answer[i][0], answer[i][1]))

	fo.close()