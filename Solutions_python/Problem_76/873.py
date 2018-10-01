#
# URL: http://code.google.com/codejam/contest/dashboard?c=351101#s=p0
#

import sys

# =====================================

def read_input(filename):

	lines = open(filename).readlines()

	line = lines[0]
	line.strip()
	num_of_testcase = int(line)
	lines = lines[1:]

	for i in range(num_of_testcase):

		line = lines[i*2].strip()
		n = int(line)

		line = lines[i*2+1].strip()
		items = line.split(" ")
		values = map(int, items)

		sum_xor = 0
		sum = 0
		for v in values:
			sum_xor ^= v
			sum += v
		if sum_xor == 0:
			print "Case #" + str(i+1) + ": " + str(sum - min(values))
			#solve_it(i+1, n, values)
		else:
			print "Case #" + str(i+1) + ": " + "NO"


# ------------------------------------

def print_debug(s):

	debug = 1
	if debug == 1:
		print s

# ------------------------------------
# ------------------------------------

# ------------------------------------

def main():
	#read_input("test.in")
	#read_input("C-small-attempt0.in")
	read_input("C-large.in")


# ====================================

if __name__ == "__main__":
	main()

