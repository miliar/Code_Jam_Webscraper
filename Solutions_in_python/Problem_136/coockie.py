#!/usr/local/bin/python2.7
def solve(C, F, X):
	total_time = 0
	prod_rate = 2.
	while True:
		time_to_buy_farm = C / prod_rate
		time_to_win = X / prod_rate
		time_to_win_after_buying = X / (prod_rate + F)
		if time_to_win > time_to_buy_farm + time_to_win_after_buying:
			# Buy a new farm
			total_time += time_to_buy_farm
			prod_rate += F
		else:
			total_time += time_to_win
			break
	return total_time

with open('input.txt') as f:
	# Error handling omitted. Supposed input format is correct.
	cases = int(f.readline().strip())
	for case in xrange(1, cases + 1):
		line = f.readline().strip()
		[C, F, X] = [float(n) for n in line.split()]
		print 'Case #%d: %.7f'%(case, solve(C, F, X))
