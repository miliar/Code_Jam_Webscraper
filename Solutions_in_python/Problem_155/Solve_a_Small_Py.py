#i = int(raw_input(''))

def readFile(fName):
	f = open(fName)
	y = f.readlines()
	f.close()
	return y

def writeFile(fName,Op):
	with open(fName, "a") as myfile:
		myfile.write(str(Op)+"\n")
	myfile.close
	
  
def findUser(sm,Si):
	required = 0
	Su=0
	for i in range(len(Si)):
		if Su >=i:
			Su=Su+Si[i]
		else:
			diff = i- Su
			required = required + diff
			Su=Su+diff+Si[i]
	return required
		
y = readFile('temp.txt')
l = 0
for j in y:	
	if l == 0:
		i = int(j)
	else:
		sm,Sa=j.split()
		sm = int(sm)
		Si = []
		for k in Sa:
			Si.append(int(k))
	
		if sm==0:
			print 0
			writeFile('fNameOp',"Case #"+str(l)+": " +str(0))
		else :
			input = findUser(sm,Si)
			print input
			writeFile('fNameOp',"Case #"+str(l)+": " +str(input))
	l = l+1
	
#for t in range(i):
#	sm,Sa=raw_input("").split()
#	sm = int(sm)
#	Si = []
#	for k in Sa:
#		Si.append(int(k))
#
#	if sm==0:
#		print 0
#	else :
#		input = findUser(sm,Si)
#		print input