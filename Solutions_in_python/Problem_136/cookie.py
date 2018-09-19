import sys
sys.setrecursionlimit(100000)

fo = open("B-small-attempt0.in", "r+")

T = 0

T = int(fo.readline())

# r: rate
# xt: goal

def min_time(r, limit):

	# print r, xt
	time_no_buy = x / r

	time_fact = c / r

	if min(time_no_buy, time_fact) >= limit:
		return limit
	elif abs(time_fact - time_no_buy) <= 0.1:
		return time_no_buy
	else:
		time_buy = time_fact + min_time(r + f, limit - time_fact)
		return min(time_buy, time_no_buy)


for i in range(T):
	c, f, x = map(float, fo.readline().split(" "))

	t = min_time(2.0, x / 2.0)
	print "Case #%d: %.7f" % (i + 1, t)