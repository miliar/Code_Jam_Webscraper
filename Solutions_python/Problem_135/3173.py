#! /usr/bin/python3

import sys;

input_filename = sys.argv[1];
output_filename = input_filename + ".out";

file_in = open(input_filename, "r");
file_out = open(output_filename, "w");

T = int(file_in.readline());
for t in range(T):
	a1 = int(file_in.readline())-1;
	print(a1)
	m1 = []
	for i in range(4):
		m1.append(file_in.readline().split());
	print(m1)
	a2 = int(file_in.readline())-1;
	print(a2)
	m2 = []
	for i in range(4):
		m2.append(file_in.readline().split());
	print(m2)
	r1 = m1[a1]
	r2 = m2[a2]
	print(r1,r2)
	common = list(set(r1).intersection(r2))

	result = ""
	if len(common) == 1:
		result = str(common[0])
	elif len(common) > 1:
		result = "Bad magician!"
	else:
		result = "Volunteer cheated!"


	file_out.write("Case #%d: %s\n" % (t+1, result))

file_in.close();
file_out.close();