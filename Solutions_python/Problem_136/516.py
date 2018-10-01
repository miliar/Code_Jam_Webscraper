def cookieStrategy(curRate, upCost, upRate, winAmount):
	time = 0

	# Check if we win before reaching decision gate
	if winAmount <= upCost:
		time = winAmount/curRate
		return time
	# Find time to next decision gate
	time = time + upCost/curRate

	while( True ):

		tStay = (winAmount - upCost) / curRate
		tUpgrade = winAmount / (curRate + upRate)

		if tStay <= tUpgrade:
			time = time + tStay
			return time
		else:
			curRate = curRate + upRate
			time = time + upCost/curRate



def main():
	numTestCases = int(raw_input())

	for n in xrange(numTestCases):
		(cost, rate, winAmount) = map(float, raw_input().split())

		# print (cost, rate, winAmount)

		time = cookieStrategy(2.0, cost, rate, winAmount)
		print "Case #{}: {:.9f}".format(n+1, time)




if __name__ == "__main__" :
	main()




