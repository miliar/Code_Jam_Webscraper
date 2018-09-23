f = open('input.in','r')
cnt = 0;
totallines = 0;

def previousTidy(lastone):
	print lastone
	
def isTidy(anum):
	tidy = True
	chars = list(str(anum))
	if len(chars) == 1:
		return True
	for c in range(0,len(chars)-1):
		if int(chars[c])>int(chars[c+1]):
			tidy = False
			break
	return tidy



for line in f:
	lastTidy = -1
	strOfLine = line.strip('\n')
	if cnt == 0:
		totallines = int(line)
		print "Total Lines: " + str(totallines);
	else:
		#print isTidy(strOfLine)
		if(isTidy(strOfLine)):
			lastTidy = int(strOfLine)
		else:
			curNum = int(strOfLine)
			while lastTidy == -1:
				curNum = curNum - 1
				if isTidy(curNum):
					lastTidy = curNum
							
		print "Case #"+str(cnt)+": " + str(lastTidy)
	cnt+=1
