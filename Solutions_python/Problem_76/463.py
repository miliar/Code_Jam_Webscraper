def res(line):
	
	candies = map(int, line.split())

	xor_list = lambda l: reduce(lambda a, b: a ^ b, l)

	return sum(candies) - min(candies) if xor_list(candies) == 0 else "NO"


if __name__ == "__main__":

	import sys

	filename = sys.argv[1]

	# Cut off case count
	caselines = open(filename).readlines()[1:]

	for case_no, line in enumerate(caselines[1::2], 1):

		print "Case #%d: %s" % (case_no, res(line))
