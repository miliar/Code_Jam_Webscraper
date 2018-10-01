#!/bin/env python3

def magic_testcase(f_in, f_out):
	n_1 = int(f_in.readline())
	# Skip first n_1 - 1 lines
	if n_1 > 1:
		for i in range(n_1 - 1):
			f_in.readline()
	l_1 = f_in.readline()

	if n_1 != 4:
		for i in range(4 - n_1):
			f_in.readline()
	

	# Do it again
	n_2 = int(f_in.readline())

	# Skip first n_1 - 1 lines
	if n_2 > 1:
		for i in range(n_2 - 1):
			f_in.readline()
	l_2 = f_in.readline()

	if n_2 != 4:
		for i in range(4 - n_2):
			f_in.readline()
	#print("Sel 1: {}, Sel 2: {}".format(l_1, l_2))

	set_1 = set( map( lambda x: int(x),l_1.split()))
	set_2 = set( map( lambda x: int(x),l_2.split()))
	set_total = set_1.intersection(set_2)

	if len(set_total) == 0:
		f_out.write("Volunteer cheated!\n")
	if len(set_total) == 1:
		f_out.write("{}\n".format(list(set_total)[0]))
	if len(set_total) > 1:
		f_out.write("Bad magician!\n")

def main(filename, fnout):
	f_in = open(filename, "rt")
	f_out = open(fnout, "wt")
	cases = int(f_in.readline())
	for i in range(cases):
		f_out.write("Case #{}: ".format(i+1))
		magic_testcase(f_in, f_out)
	f_out.close()

main("input-01.txt", "output-01.txt")
