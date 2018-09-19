import sys

def main(input_file):
	number_of_cases = int(input_file.readline().strip("\n"))
	for case_number in xrange(1, number_of_cases + 1):
		print "Case #%d: %s" % (case_number, case(input_file))

def case(input_file):
	C, F, X = [float(value) for value in input_file.readline().strip("\n").split(" ")]
	T = int(X/C - 2.0/F)
	if T < 0 : T = 0
#	from pdb import set_trace; set_trace()
	dur = X / (2.0 + F * T)
	for i in xrange(T):
		dur += C * (1.0 / (2 + F * i))
	return "%.7f" % (dur, )

if __name__ == '__main__':
	main(open(sys.argv[1]))


