#!/usr/bin/python
import sys
file = open('bot-data','r')
t = int(file.readline())
for x in range(t):
	l = file.readline()
	oList = []
	bList = []
	order = []
	oPos = 1
	bPos = 1
	time = 0
	l = l[:len(l)-1]
	numbers = l.replace('B','').replace('O','')
	numbers = [int(j) for j in numbers.split()]
	numbers.pop(0)
	for i in range(len(l)):
		if l[i] == 'O':
			order.append('O')
			oList.append (numbers.pop(0))
			continue
		if l[i] == 'B':		
			order.append('B')
			bList.append (numbers.pop(0))
	#print 'oList: ',oList
	#print 'bList: ',bList
	#print 'order: ',order
	pressed = 0
	while len(order) > 0:
		if len(oList) > 0:
			if oPos > oList[0]:
				oPos -= 1
				#print 'O back to ',oPos
			elif oPos < oList[0]:
				oPos += 1		
				#print 'O moved to ',oPos
			elif oPos == oList[0] and order[0] == 'O':
				pressed = 1
				oList.pop(0)
				#print 'O pressed button on ',oPos
			#else: print 'O stays on ',oPos
	
		if len(bList) > 0:
			if bPos > bList[0]:
				bPos -= 1
				#print 'B back to ',bPos
			elif bPos < bList[0]:
				bPos += 1
				#print 'B moved to ',bPos
			elif bPos == bList[0] and order[0] == 'B':
				pressed = 1
				bList.pop(0)
				#print 'B pressed button on ',bPos
			#else: print 'B stays on ',bPos

		time += 1
		if pressed == 1: 
			order.pop(0)
			pressed = 0
	sys.stdout.write('Case #')
	sys.stdout.write(str(x+1))
	print ":",time
	
	
