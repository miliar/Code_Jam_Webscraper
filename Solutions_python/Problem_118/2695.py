import sys, math

def is_palindrome(num):
	num_arr = list(str(num))

	while True:
		try:
			first = num_arr.pop(0)
			last  = num_arr.pop()

			if first != last:
				return False
		except IndexError, e:
			break

	return True

fname = sys.argv[1]

f = open(fname, 'r')

num_cases = int(f.readline())

for case in range(0, num_cases):
	params = f.readline().split(" ")
	start = int(params[0])
	stop  = int(params[1])

	num_fair_square = 0
	for i in range(start, stop+1):
		if is_palindrome(i):
			sqr = math.sqrt(i)
			sqr_arr = list(str(sqr))
			# check to see if rounding this to an int is valid...
			if sqr_arr.pop() == "0":
				if sqr_arr.pop() == ".":
					sqr = int(sqr)
					if is_palindrome(sqr):
						num_fair_square += 1

	print "Case #%d: %d" % (case+1, num_fair_square)