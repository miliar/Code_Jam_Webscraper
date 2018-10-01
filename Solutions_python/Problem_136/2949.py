import math

def should_buy(total_time, rate, buy_rate, C, F, X):
	waiting_time = total_time + (X / rate)
	buy_time = total_time + (C / rate) + X / (F + rate)
	#print "Decide between %s and %s. Total: %s, X: %s, rate: %s" % (waiting_time, buy_time, total_time, rate, X)
	return buy_time < waiting_time

def min_time(C, F, X):
	# C: price of farm
	# F: farm rate
	# X: target
	initial_rate = 2 # 2 cookies per second
	current_rate = initial_rate
	buy_rate = current_rate + F
	total_time = 0

	while should_buy(total_time, current_rate, buy_rate, C, F, X):
		total_time += (C / current_rate)
		#print "buy. total time is now %s. C is %s and cur rate is %s" % (total_time, C, current_rate)
		#print "adding %s" % (C / current_rate)
		current_rate += F
		buy_rate = current_rate + F
	total_time += (X / current_rate)

	return str(round(total_time, 7))

def main():
	f = open('/Users/alex/Downloads/B-large.in.txt')
	nTests = int(f.readline().replace("\n",""))

	for i in range(nTests):
		numbers = f.readline().replace("\n","").split(" ")

		print "Case #" + str(i+1) + ": " + min_time(float(numbers[0]), float(numbers[1]), float(numbers[2]))


if __name__ == "__main__":
    main()
