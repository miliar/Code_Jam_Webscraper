from decimal import *

filename = raw_input('Enter a file name: ')

with open(filename) as fp:
    content = fp.read().splitlines()

testCases = content.pop(0)

baseRate = 2

for a in range(0, int(testCases)):
	case = content.pop(0).split(" ")
	case = [ float(y) for y in case ]
	C,F,X = case
	#C is cost of farm
	#F is cookies per second each farm provides
	#X is number of cookies needed to win
	
	times=[]
	times.append(X / baseRate) #no purchases
	
	timeNeededToBuy=[] #will store the time to buy n farms
	timeNeededToBuy.append(0.00)
	
	for z in range(1, int(X)):
		rate = baseRate + (F*(z-1))
		timeNeededToBuy.append(timeNeededToBuy[z-1] + C/rate)
		#then, assuming I buy z farms, the time needed is the time to buy those z farms plus the time remaining to generate the cookies
		totalTime = timeNeededToBuy[z-1] + X/rate
		
		if totalTime > min(times):
			break
		else:
			times.append(totalTime)
			
	answer = Decimal(min(times)).quantize(Decimal('.0000001'))
	
	print "{}{}{}{}".format("Case #", a+1,": ", answer)
	
	