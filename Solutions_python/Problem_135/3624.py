import sys

def match(firstline, secondline, numcase):
	o = open('output.txt', 'a')	
	firsttime = firstline.split()
	secondtime = secondline.split()

	thirdtime = list(set(firsttime) & set(secondtime))
	if len(thirdtime) > 1:
		o.write('Case #%d: Bad magician!\n' % numcase)
	
	elif len(thirdtime) == 0:
		o.write('Case #%d: Volunteer cheated!\n' % numcase)

	else: 
		o.write('Case #%d: %s\n' % (numcase, thirdtime[0]))
	
def mainrecurse(fname):
	f = open(fname, 'r')
	numcases = int((f.readline()))
	for i in range(numcases):
		firststring = ''
		x = int((f.readline()))
		for j in range(4):
			if(j == x-1):
				firststring = f.readline()
			else: 
				f.readline()

		secondstring = ''
		y = int(f.readline())
		for j in range(4):
			if(j == y-1):
				secondstring = f.readline()
			else:
				f.readline()
		match(firststring, secondstring, i+1)
		
						
if __name__ == "__main__":
	mainrecurse(sys.argv[1])
	
