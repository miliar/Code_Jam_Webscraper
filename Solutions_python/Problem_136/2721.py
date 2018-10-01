import csv
import math
with open('B-large.in', 'rb') as cookies:
	table = csv.reader(cookies, delimiter=' ')
	for t in xrange(int(table.next()[0])):
		test = table.next()
		C = float(test[0])
		F = float(test[1])
		X = float(test[2])
		seconds = X/2
		f = 2
		while True:
			tmp = seconds - (X-C)/f
			f += F
			tmp += X/f
			if (tmp > seconds):
				print "Case #" + str(t+1) + ": " + str(seconds)
				break
			else:
				seconds = tmp