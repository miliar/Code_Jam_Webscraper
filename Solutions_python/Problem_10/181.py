#!/usr/bin/python

import sys

if len(sys.argv) <= 1:
	print "Please provide an input file"
	sys.exit(1)

input_file_name = sys.argv[1]
input_file = file(input_file_name, "r")
output_file = file("output1.txt", "w")

testcases = int(input_file.readline())

for testcase in range(testcases):
	letters_on_key, keys, letters = [int(x) for x in input_file.readline().split(" ")]
	frequency = [int(x) for x in input_file.readline().split(" ")]
	
	frequency.sort(reverse=True)
	hits = 0
	key_press_count = 1
	for i in range(0, len(frequency)):
		hits = hits + frequency[i] * key_press_count
		if (i+1) % keys == 0:
			key_press_count = key_press_count + 1
	
	output_file.write("Case #%s: %s\n" % (testcase + 1, hits))

output_file.close()