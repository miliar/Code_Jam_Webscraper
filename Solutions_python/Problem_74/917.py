import sys

def readInputNo(input):
	file = open(input, "r")
	inputno = int(file.readline().strip('\n'))
	file.close()
	return inputno
	
def readData(input):
	file = open(input, "r")
	file.readline()
	data = {}
	i=0
	data = []
	data = file.readlines()
	return data
	
def readCommands(robot,command):
	command = command.strip('\n')
	command = command.split(' ')
	commands = []
	
	i=0
	count=0
	for char in command:
		if (char == 'O' or char == 'B'):
			count+=1
			if (char == robot):
				#first no is the count, second is which button need to be pressed.
				commands.append((count,int(command[i+1])))
		i+=1
	return commands
	
def checklock(O, B, counter):
	for command in O:
		if command[0] == counter:
			return 'O'
	for command in B:
		if command[0] == counter:
			return 'B'
	return 'NULL'		
	
def setGlobals():
	global lock, o, b, locO, locB
	lock = ''
	o=0
	b=0
	locO=1
	locB=1


		
def main():
	inputno = readInputNo(sys.argv[1])
	debugstr = ""
	data = readData(sys.argv[1])
	case = 0
	input = data[14]
	#print input
	#if(1==1):
	for input in data:
		case+=1
		noC = int(input.split(' ')[0])
		B = readCommands('B', input)
		O = readCommands('O', input)
		#setGlobals()
		#print 'O: ', O
		#print 'B: ', B
		count=0
		counter = 1
		o=0
		b=0
		locO=1
		locB=1
		while(counter<=noC):
			count+=1
			lock = checklock(O, B, counter)
			if(O != []):
				if(locO < O[o][1]):
					locO+=1
					debugstr+= "Orange moves to button " + str(locO) +"\n"
				elif(locO > O[o][1]):
					locO-=1
					debugstr+= "Orange moves to button " + str(locO) +"\n"
				else:
					if (lock == 'O'):
						counter+=1
						if(o<len(O)-1):
							o+=1
							debugstr+= "Orange pushes button " + str(locO) +"\n"
					else:
						debugstr+= "Orange stayes at button " + str(locO) + "\n"
			if(B != []):
				if(locB < B[b][1]):
					locB+=1
					debugstr+=	 "Black moves to button " + str(locB) + "\n"
				elif(locB>B[b][1]):
					locB-=1
					debugstr+= "Black moves to button " + str(locB) + "\n"
				else:
					if (lock == 'B'):
						counter+=1
						if(b<len(B)-1):
							b+=1
						debugstr+= "Black pushes button " + str(locB) + "\n"
					else:
						debugstr+= "Black stayes at button " + str(locB)		+"\n"
	#	print debugstr	
	#	print locO
	#	print locB
	#	print noC
		print ("Case #%d:"  %case), count
	


main()


