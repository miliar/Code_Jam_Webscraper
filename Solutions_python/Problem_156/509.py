#global minimunValue

import sys
def func(PancakesOnS, time, maxTime ) :
	#print 'tc, PancakesOnS, time', tc,  PancakesOnS, time
	global minimunValue
	#print 'minimunValue', minimunValue
	if maxTime <= time or minimunValue <= time: return maxTime

	if max(PancakesOnS) <= 0: return time

	if max(PancakesOnS)<=3:
		PancakesOnS = [PancakesOnS[i]-1 for i in range(len(PancakesOnS))]
		return func(PancakesOnS, time+1, maxTime)
	else:
		#print PancakesOnS
		oneMax = max(PancakesOnS)

		#minimunValue = sys.maxint
		for serverGive in range(2,max(PancakesOnS)/2+1):
			PancakesOnS2 = PancakesOnS[:]
			PancakesOnS2[PancakesOnS2.index(oneMax)] -= serverGive
			PancakesOnS2.append(serverGive)
			minimunValue = min(minimunValue, func(PancakesOnS2, time+1, maxTime))

		PancakesOnS3 = PancakesOnS[:]
		PancakesOnS3 = [PancakesOnS3[pos]-1 for pos in range(len(PancakesOnS3))]
		minimunValue = min(minimunValue, func(PancakesOnS3, time+1, maxTime))

		###


		#max(PancakesOnS)
	return minimunValue


	#if 


	#print 'PancakesOnS', PancakesOnS






def displayArray(my_array):
	for i in range(len(my_array)):
		print i

for tc in range(1, int(raw_input())+1):
	#print 
	minimunValue = sys.maxint

	y = ''
	#print

	D = int(raw_input())
	#D, the number of diners with non-empty plates, 
	#another line with D space-separated integers representing the numbers of pancakes on those diners' plates.

	PancakesOnS = map(int,raw_input().split())
	#print PancakesOnS

	#print 'PancakesOnS', PancakesOnS
	y= func(PancakesOnS, 0, max(PancakesOnS)) 


	#y is the smallest number of minutes needed to finish the breakfast.
	#if y != ''
	print "Case #{}: ".format(tc) + str(y)
	#else:
	#print "Case #{}".format(tc) + stry(y)
		
	
