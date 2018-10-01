import sys
import time

fin = sys.stdin
T = int(fin.readline())
for case in range(1,T+1):
	buttons = str(fin.readline()).split()
	t = 0
	presses = 0
	try:
		blue = buttons.index("B")+1
		bluenext = int(buttons[blue])
		blueloc = 1
		bluedist = abs(bluenext - blueloc)

	except ValueError:
		blue = int(buttons[0])*2+1
		bluedist = 0
	try:
		orange = buttons.index("O")+1
		orangenext = int(buttons[orange])
		orangeloc = 1
		orangedist = abs(orangenext - orangeloc)

	except ValueError:
		orange = int(buttons[0])*2+1
		orangedist = 0	
	while presses < int(buttons[0]):
		if blue < orange:
			if bluedist + 1 < orangedist:
				orangedist = orangedist - (bluedist+1)
			else:
				orangedist = 0
			t = t + bluedist + 1
			blueloc = bluenext
			presses = presses + 1
			try:
				blue = buttons.index("B",blue)+1
				bluenext = int(buttons[blue])
				bluedist = abs(bluenext - blueloc)
			except ValueError:
				blue = int(buttons[0])*2+1
				
		else:
			if orangedist + 1 < bluedist:
				bluedist = bluedist - (orangedist+1)
			else:
				bluedist = 0
			t = t + orangedist + 1
			orangeloc = orangenext
			presses = presses + 1
			try:
				orange = buttons.index("O",orange)+1
				orangenext = int(buttons[orange])
				orangedist = abs(orangenext - orangeloc)
			except ValueError:
				orange = int(buttons[0])*2+1
	
	print "Case #{0}: {1}".format(case,t) 
