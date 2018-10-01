def change(alist,aindex):
	
	alist[aindex-1] = alist[aindex-1] -1
	if alist[aindex-1] == 0 and aindex==1:
		alist.pop(0)
		aindex -=1
	length = len(alist)
	for i in range(aindex,length):
		alist[i] = 9
	return alist

def listToString(alist):
	x = ""
	for i in alist:
		x = x+str(i)
	return x

def lastTidy(snumber):
	if len(snumber) == 0:
		return snumber
	lnumber = [int(i) for i in snumber]
	length = len(lnumber)
	for i in range(length-1):
		if lnumber[i] > lnumber[i+1]:
			lnumber = change(lnumber,i+1)
			lasttidy =  listToString(lnumber)
			return lastTidy(lasttidy)
	return snumber		
	


tasklist=[]
lines = [line.rstrip('\n') for line in open('q2.inp')]
taskcount=int(lines.pop(0));
for i in range(taskcount):
	inlist =lines.pop(0).split(" ")
	snumber=inlist[0]
	res=lastTidy(snumber)
	print ("Case #"+str(i+1)+": "+res)
