#!/usr/bin/env python
import sys
def main():
	inputfile = open(sys.argv[1], "r")
	numberOfCases = int(inputfile.readline()[:-1])
	case = 0
	for line in range(numberOfCases):
		case += 1
		lineContents = inputfile.readline()[:-1].split()
		numberOfSwitches = int(lineContents[0])
		lineContents = lineContents[1:]
		switches = []
		colours = []
		orangeSwitches = []
		blueSwitches = []
		for s in range(numberOfSwitches):
			#print 'colour', lineContents[s*2], 'switch', lineContents[(s*2)+1]
			switches += [int(lineContents[(s*2)+1])]
			colours += [lineContents[(s*2)]]
			if lineContents[s*2] == 'B':
				blueSwitches += [int(lineContents[(s*2)+1])]
			else:
				orangeSwitches += [int(lineContents[(s*2)+1])]
		#print 'colour', colours, 'switch', switches 
		bluePos = 1
		orangePos = 1
		time = 0
		blueDone = False
		orangeDone = False
		#for i in range(len(switches)):
			#print colours[i], switches[i]
		b = 0
		o = 0
		buttonTurn = ''
		i = 0
		while not (blueDone and orangeDone):
			time +=1
			#print '--------'
			try:
				targetBlue = blueSwitches[b]
			except IndexError:
				blueDone = True
			try:	
				targetOrange = orangeSwitches[o]
			except IndexError:
				orangeDone = True
				
			#print targetBlue, bluePos, targetOrange, orangePos, blueDone, orangeDone
			#print 'b', b, 'o', o
			buttonTurn = colours[i]
			if not blueDone:
				if bluePos == targetBlue:
					if buttonTurn == 'B':
						#print 'blue - push button at', bluePos
						b += 1
						i += 1
						if b >= len(blueSwitches):
							blueDone = True
					else:
						pass
						#print 'blue - wait at', bluePos
						
				elif bluePos < targetBlue:
					bluePos += 1
					#print 'blue moves forewards to', bluePos
				elif bluePos > targetBlue:
					bluePos -= 1
					#print 'blue moves backwards to', bluePos

			if not orangeDone:
				if orangePos == targetOrange:
					if buttonTurn == 'O':
						#print 'orange - push button at', orangePos
						o += 1
						i += 1
						if o >= len(orangeSwitches):
							orangeDone = True
					else:
						pass
						#print 'orange - wait at', orangePos
						
				elif orangePos < targetOrange:
					orangePos += 1
					#print 'orange moves forewards to', orangePos
				elif orangePos > targetOrange:
					orangePos -= 1
					#print 'orange moves backwards to', orangePos
					
		print 'Case #%s: %s' % (case, time)
if __name__ == '__main__':
	main()
