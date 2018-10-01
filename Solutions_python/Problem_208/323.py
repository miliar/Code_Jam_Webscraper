import os
import sys
import decimal

num_cities = None
horses = [None]
d = {}
num_interested = 0
num_distances = 0
interested = []

decimal.getcontext().prec=100

def solve():
#	print horses, d, interested
	best = {}
	num_cities = len(horses) - 1
	best[num_cities] = 0	
	for city in xrange(num_cities - 1, 0, -1):
#		print "CITY", city
		dist, speed = horses[city]
#		print "horse", dist, speed
		speed = decimal.Decimal(speed)
		to_city = city+1
		best_found = to_city
		best_time = best[to_city] + d[city,to_city]/speed
		dist_so_far = d[city,to_city]
		to_city += 1
#		print "best_found", best_found, best_time
		while to_city <= num_cities and dist >= (dist_so_far + d[to_city-1, to_city]):
			dist_so_far += d[to_city-1, to_city]
			t = best[to_city] + dist_so_far / speed
			if t < best_time:
				best_time = t
				best_found = to_city
#				print "overrule", best_found, best_time
			to_city += 1

		best[city] = best_time

#	print best

	return "%.8f" % (best[1],)

def interleave(s1,s2):
	l = list(s1)
	for i,a in enumerate(s2):
		l[i % len(l)] += a
	return ''.join(l)

def process_line(l, i):
	global num_cities, num_interested, num_distances, d, horses
	if i == 0:
		num_tests = int(i)
	elif num_cities == None:
		num_cities, num_interested = [int(a) for a in l.split(' ')]
	elif num_cities > 0:
		horses.append([int(a) for a in l.split(' ')])
		num_cities -= 1

	elif num_distances < len(horses) - 1:
		num_distances += 1
		distances = [int(a) for a in l.split(' ')]
		for i,di in enumerate(distances):
			if di == -1:
				continue
			d[num_distances, i+1] = di

	elif num_interested > 0:
		num_interested -= 1
		interested.append([int(a) for a in l.split(' ')])
		if num_interested == 0:
			r = solve()
			num_cities = None
			num_distances = 0
			horses = [None]
			return r

def main():

	fn = sys.argv[1]
	fn_out = sys.argv[2]
	lines = open(fn, 'rb').read().splitlines()
	out_fd = open(fn_out, 'wb')
	i = 0
	case_num = 0
	for line in lines:
		s = process_line(line, i)
		i += 1
		if s is not None:
			case_num += 1
			out_fd.write('Case #%d: %s' % (case_num, s))
			out_fd.write('\n')

if __name__ == "__main__":
	main()


"""
"""