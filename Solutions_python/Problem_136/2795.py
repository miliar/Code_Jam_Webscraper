
def answer(C, F, X):
	total_seconds = 0
	rate = 2
	seconds_if_wait = X / rate
	seconds_if_purchase = (C / rate) + (X / (rate+F))
	while 1:
		if seconds_if_wait < seconds_if_purchase:
			total_seconds += seconds_if_wait
			return total_seconds
		else:
			total_seconds += C / rate
			rate += F
			seconds_if_wait = X / rate
			seconds_if_purchase = (C / rate) + (X / (rate+F))

with open('B-large.out', 'w') as z:
	with open('B-large.in', 'r') as y:
		num_cases = int(y.readline().strip())
		for i in range(num_cases):
			c, f, x = y.readline().strip().split()
			z.write('Case #%s: %.7f\n' %(i+1,answer(float(c), float(f), float(x))))