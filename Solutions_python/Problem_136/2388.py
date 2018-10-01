#!/usr/bin/python

def time_till(cookie_rate, cookies_wanted):
	return cookies_wanted / cookie_rate

def main():
	T = int(raw_input())
	for i in range(1, T + 1):
		print('Case #' + str(i) + ': ' + answer())

def answer():
	C, F, X = [float(x) for x in raw_input().split()]
	ttime = 0.0 # Total time taken
	rate = 2.0 # The rate at which cookies are produced
	while True:
		time_no_farm = time_till(rate, X)
		time_with_farm = time_till(rate, C) + time_till(rate + F, X)
		if time_no_farm <= time_with_farm:
			ttime += time_no_farm
			return str(ttime)
		else:
			# Buy a farm
			ttime += time_till(rate, C)
			rate += F

main()
