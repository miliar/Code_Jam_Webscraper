warPoint = 0
dWarPoint = 0
def convert (x):
	x = x.split()
	x = [float(i) for i in x]
	return x

def War(weightN,weightK):
	global warPoint 
	if len(weightN) == 0:
		return warPoint 
	else:
		chosen_n = weightN[-1]
		if chosen_n > weightK[-1]:
			weightK.pop(0)
			weightN.pop()
			warPoint += 1
			
			War(weightN,weightK)
		else:
			weightK.pop(-1)
			weightN.pop(-1)
			
			War(weightN,weightK)

def Dwar(weightN,weightK):
	global dWarPoint
	if len(weightN) == 0:
		return dWarPoint
	else:
		chosen_n = weightN[-1]
		if chosen_n > weightK[-1]:
			for i in weightND:
                        	if i > weightKD[0]:
                                	test = i
                                        break

                        weightKD.pop(0)
                        weightND.pop(weightND.index(test))
                        dWarPoint += 1
			Dwar(weightN,weightK)
		else:
			weightK.pop()
			weightN.pop(0)
			Dwar(weightN,weightK)
	


if __name__ == '__main__' : 
	count = input()
	i = 0
	while(i<count):
		n = input()
		weight = raw_input()
		weightN = convert(weight)
		weight = raw_input()
		weightK = convert(weight)
	#	weightN = [0.186,0.389,0.907,0.832,0.959,0.557,0.300,0.992,0.899]
	#	weightK = [0.916,0.728,0.271,0.520,0.700,0.521,0.215,0.341,0.458]
		weightN.sort()
		weightK.sort()
		weightND = []
		weightKD = []
		for j in weightN:
			weightND.append(j)
		for j in weightK:
			weightKD.append(j)
		warPoint = 0
		dWarPoint = 0
		#War(weightN,weightK,warPoint)
		test1 =  Dwar(weightND,weightKD);
		test2 = War(weightN,weightK);	
		print "Case #"+(str)(i+1)+": "+(str)(dWarPoint)+" "+ (str)(warPoint)
		#print "Case #"+(str)(i+1)+": "+(str)(dWarPoint)+" "+(str)(war)
		#print weightND,"\n",weightKD
		i+=1

