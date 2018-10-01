import sys

sys.stdin = open("cookie_clicker_large.in", "r")
sys.stdout = open("cookie_clicker_large.out", "w")

cases = int(raw_input())

for case in xrange(1, cases + 1):

	nums = raw_input().split()

	C = float(nums[0])
	F = float(nums[1])
	X = float(nums[2])

	# initial values
	income = 2
	cookies = 0
	seconds = 0.

	while True:
		
		seconds += C / income
		
		# now we're at a point where we can buy a farm. Is it worth it?
		if (X / (income + F)) < ((X - C) / income):
			# worth it!
			income += F

		else:
			# did not buy a farm, calculate how long we should sit at this
			# income level to reach the goal then break
			seconds += (X - C) / income
			break

	print "Case #%d: %f" % (case, seconds)