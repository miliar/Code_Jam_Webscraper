#!/usr/bin/env python
# Run file like so:
# 	python filename.py input.in

import sys

def main(args):

	# File to read
	input_file = "A-large.in"
	if (len(args) > 0):
		input_file = args[0].strip()

	# Open files
	f_in = open(input_file, 'r')
	f_out = open('output.txt', 'w')

	# Get number of cases
	cases = int(f_in.readline().strip())

	# Print all cases
	for i in range(1, cases+1):
		result = doCase(f_in)

		if not result:
			print "Error"
			sys.exit(0)

		printResult(f_out, i, result)


def doCase(f_in):
	line = f_in.readline().strip().split(None)
	D = int(line[0])
	N = int(line[1])

	# DEBUG
	#print D, N

	slowest_time = None
	annie_travel = 0

	for i in range(N):
		sub_line = f_in.readline().strip().split(None)
		K_i = int(sub_line[0])
		K_s = int(sub_line[1])

		# DEBUG
		#print K_i, K_s

		travel_distance = (D - K_i)
		time = float(travel_distance) / K_s

		if slowest_time is None:
			slowest_time = time

		else:
			slowest_time = max(slowest_time, time)

		#print slowest_time

	annie_travel = float(D) / slowest_time
	return "%.6f" % annie_travel

# Print result in the specific case format
def printResult(f_out, case_no, result):
	f_out.write("Case #%d: " % case_no)

	# SPECIFIC PRINT FORMAT HERE
	f_out.write("%s" % result)

	f_out.write("\n")

if __name__ == '__main__':
	main(sys.argv[1:])
