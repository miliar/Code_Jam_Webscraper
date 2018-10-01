# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.


def last_tidy(n):

	l = [int(d) for d in list(str(n))]

	if l == sorted(l):
		return n

	last_l = [l[0] - 1] + [9] * (len(l) - 1)

	for i in range(1, len(l)):
		new_l = l[:i] + [l[i] - 1] + [9] * (len(l) - i -  1)

		if new_l != sorted(new_l):
			return int("".join([str(i) for i in last_l]))
		last_l = new_l


t = int(raw_input())  # read a line with a single integer


for i in xrange(1, t + 1):
  n = int(raw_input()) 


  print "Case #{}: {}".format(i, last_tidy(n))