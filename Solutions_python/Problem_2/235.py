#! /usr/bin/env python
f=open('B-large.in', 'r')
f2=open('B-large.out','w')
intQNumber=int(f.readline())
for intLoopCount in range(intQNumber):
	intTurnTime=int(f.readline())
	a=f.readline()
	intDepartA=int(a[:a.find(' ')])
	intDepartB=int(a[(a.find(' ')+1):])
	lstDepartA=range(intDepartA)
	lstDepartB=range(intDepartB)
	lstArriveA=range(intDepartB)
	lstArriveB=range(intDepartA)
	for intCount in range(intDepartA):
		a=f.readline()
		lstDepartA[intCount]=int(a[0:2])*60+int(a[3:5])
		lstArriveB[intCount]=int(a[6:8])*60+int(a[9:11])+intTurnTime
	for intCount in range(intDepartB):
		a=f.readline()
		lstDepartB[intCount]=int(a[0:2])*60+int(a[3:5])
		lstArriveA[intCount]=int(a[6:8])*60+int(a[9:11])+intTurnTime
	lstDepartA.sort()
	lstDepartB.sort()
	lstArriveA.sort()
	lstArriveB.sort()


	#Computing Number of Trains Needed at A
	intNumReturn=0
	intDepartCount=0
	for intCount in range(intDepartB):
		if intDepartA==0:
			break
		bolFlag=True
		bolFlag2=False
		while bolFlag:
			if lstArriveA[intCount]<=lstDepartA[intDepartCount]:
				bolFlag=False
				intNumReturn+=1
			intDepartCount+=1
			if intDepartCount==intDepartA:
				bolFlag=False
				bolFlag2=True
		if bolFlag2:
			break
	intATrain=intDepartA-intNumReturn


	#Computing Number of Trains Needed at B
	intNumReturn=0
	intDepartCount=0
	for intCount in range(intDepartA):
		if intDepartB==0:
			break
		bolFlag=True
		bolFlag2=False
		while bolFlag:
			if lstArriveB[intCount]<=lstDepartB[intDepartCount]:
				bolFlag=False
				intNumReturn+=1
			intDepartCount+=1
			if intDepartCount==intDepartB:
				bolFlag=False
				bolFlag2=True
		if bolFlag2:
			break
	intBTrain=intDepartB-intNumReturn
	
	f2.write('Case #'+str(intLoopCount+1)+': '+str(intATrain) +' '+str(intBTrain)+'\n')
f.close()
f2.close()
