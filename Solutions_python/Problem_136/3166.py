#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from decimal import Decimal

def readline(f):
	return f.readline()[:-1]

def run_program(in_file, out_file):
	cases = int(readline(in_file))
	cookie_rate = Decimal('2.000000000')
	print 'Cases: ', cases
	for i in range(0, cases):
		#c: Cost of Cookie Farm
		#f: Cookie Farm extra rate
		#x: Target
		c, f, x = [Decimal(num) for num in readline(in_file).split(' ')]
		completed = False
		res = Decimal('0.000000000')
		current_cookie_rate = cookie_rate

		#max_time_limit = x/cookie_rate
		#farm_time = c/current_cookie_rate
		current_cookies = 0
		current_time = Decimal('0.00000000')
		while not completed:
			time_next_farm = (c - current_cookies)/current_cookie_rate
			time_to_target_if_purchase_farm = time_next_farm + x/(current_cookie_rate + f)
			time_to_target_current = ((x - current_cookies)/current_cookie_rate)
			if time_to_target_if_purchase_farm < time_to_target_current:
				current_time += time_next_farm
				current_cookie_rate += f
				current_cookies = 0
			else:
				current_time += time_to_target_current
				completed = True
		print 'Case', (i+1), current_time
		out_file.write("Case #%d: %f\n" % (i+1, current_time))

if __name__ ==  "__main__":
	if len(sys.argv) == 3:
		f = open(sys.argv[1], 'r')
		o = open(sys.argv[2], 'w')
		run_program(f, o)
		f.close()
		o.close()
	else:
		print u"Número de parámetros incorrecto. Se esperan 2."
		print str(sys.argv)

