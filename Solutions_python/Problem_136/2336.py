import collections
import sys

fout = open(sys.argv[2],'w')

with open(sys.argv[1],'r') as f:
    	numTests = int(f.readline())
	#print numTests
	#print '-------------------'
	testNum = 0

	while True:
		testNum += 1
		testParamLine = f.readline()
		if not testParamLine:
			break
		testParams = testParamLine.rstrip().split(' ');
		#print testParams 
		#print '------------------'
		C = float(testParams[0])
		F = float(testParams[1])
		X = float(testParams[2])
		#print C
		#print F
		#print X
		#print '+++++++++++++++++'
		totalSeconds = 0
		currentRate = 2
		i = 0
		#print '#################'
		bestTimeToCollect = 0
		if X <= C:
			#print 'BESTTIME >>>>>>>'
			fout.write('Case #' + str(testNum) + ': ' + '{:.7f}'.format(round((X / 2), 7)) + '\n')
			continue
		elif i==0:
			a, b = divmod(X, C)
			bestTimeToCollect = (C/2*a) + (b/2)
			#print 'init -> bestTimeToCollect'
			#print round(bestTimeToCollect, 7)
		while True:
			#print '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
			seconds = C / (2 + (i * F))
			currentRate += F
			totalSeconds += seconds
			remainingTimeAtCurrentRate = X / currentRate
			timeToComplete = totalSeconds + remainingTimeAtCurrentRate
			#print i 
			#print seconds
			#print currentRate
			#print totalSeconds
			#print remainingTimeAtCurrentRate
			#print timeToComplete
			if(bestTimeToCollect > timeToComplete):
				bestTimeToCollect = timeToComplete
			else:
				#print 'BESTTIME >>>>>>>>>'
				fout.write('Case #' + str(testNum) + ': ' + '{:.7f}'.format(round(bestTimeToCollect, 7)) + '\n')
				break
			i += 1
				
fout.close()
#print 'fin!'

