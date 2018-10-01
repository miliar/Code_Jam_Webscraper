#!/usr/bin/env python


# Get the number of test cases, T.
T = int( raw_input() )
# Process each test case.
for case in xrange( 0, T ):
	# Get the values of C, F and X.
	values = raw_input().split()
	C = float( values[ 0 ] )
	F = float( values[ 1 ] )
	X = float( values[ 2 ] )
	# The objective is to get the minimum number of seconds, s, needed to
	# accumulate X cookies. At first, this may seem like a daunting task
	# with infinite possibilities. However, the following 2 points will
	# help in greatly simplifying the problem.
	#
	# Point #1: There is a generalized formula we can use for determining
	# s as long as we set the number of cookie farms we intend to buy.
	#
	# If we choose not to buy any cookie farms, we'll need X / 2 seconds
	# to reach our cookie goal.
	#
	# No farms bought: s = X / 2
	#
	# If we choose to buy 1 cookie farm, we'll need C / 2 seconds to raise
	# cookie funds to purchase the farm. That seems like extra time but the
	# added cookie production may offset it. With the farm helping out, only
	# X / ( 2 + F ) more seconds will be needed before we reach our goal.
	#
	# 1 farm bought: s = C / 2 + X / ( 2 + F )
	#
	# It's possible that we can get an even better time by buying a second
	# cookie farm. To pull off the 2-farm solution, we'll need C / 2 seconds
	# to save up for the first farm, C / ( 2 + F ) seconds to raise funds for
	# the second farm and then X / ( 2 + 2 * F ) seconds to accumulate enough
	# cookies to reach our goal.
	#
	# 2 farms bought: s = C / 2 + C / ( 2 + F ) + X / ( 2 + 2 * F )
	#
	# We can go on and on here if we want to but the above should be enough to
	# show that there is a pattern to calculating the total time s based on the
	# number of cookie farms purchased. Supposing we plan to purchase n cookie
	# farms, the total time s can be computed as shown below.
	#
	# s = C / 2 + C / ( 2 + F ) + C / ( 2 + 2 * F ) + ... +
	#     C / ( 2 + ( n - 1 ) * F ) + X / ( 2 + n * F )
	#
	# The above is the generalized formula we can use. This completes point #1.
	#
	# Although having a formula helps, there are still so many possibilities to
	# consider. What if we don't buy any farms? What if we get 1? Or a hundred?
	# Or a thousand? Is there a way we can keep computational effort to a
	# reasonable amount?
	#
	# Point #2: We can start with no farms and then compute s adding one farm
	# at a time. As long as we get decreasing values of s while we add farms,
	# we can continue. Once the value of s starts increasing, we can stop. The
	# lowest value of s we got ought to be the minimum number of seconds we
	# need to achieve the cookie goal.
	minimumS = None  # we take note of the best time we have so far
	n = 0  # this represents the number of cookie farms we intend to buy
	# Below is the total time we need to spend to purchase our desired number
	# of cookie farms. It seems better to accumulate this value outside the loop
	# so that we can save time avoiding repetitive calculations.
	timeToBuyFarms = 0
	while True:
		# Add the time we need to buy the nth cookie farm.
		if n > 0:
			timeToBuyFarms += C / ( 2 + ( n - 1 ) * F )
		# Add the time we need to reach our cookie goal.
		s = timeToBuyFarms + X / ( 2 + n * F )
		# Check the resulting time with previous results.
		if minimumS is not None:
			if s <= minimumS:
				# The time value is not yet increasing so we can try adding
				# more cookie farms. This is also the best time so we take
				# note of it.
				minimumS = s
			else:
				# The time value is starting to increase. This will only get
				# worse as we add more farms so we should stop here and go
				# with the best time value we got.
				break
		else:
			# No previous result yet so we take note of this one.
			minimumS = s
		# On the next iteration, we try with 1 additional cookie farm to see
		# if we can get a better time.
		n += 1
	# Provide the best time value we got.
	print "Case #%d: %.7f" % ( case + 1, minimumS )

