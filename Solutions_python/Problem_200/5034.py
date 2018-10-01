global firstLine
global good
global lastValue
global case
firstLine = True
good = True
lastValue = None
case = 1
with open("/home/fabian/file.in") as f:
	for line in f:
		if firstLine:
			firstLine = None 
			continue
		max = int(line)
		for x in range(max+1):
			firstDigit = True
			good = True
			value = x
			digits = []
			lastDigit = None
			while(value > 0):
				digits.append(value % 10)
				value /= 10
			for y in digits:
				if firstDigit:
					firstDigit = None
					lastDigit = y
				else:
					if y >  lastDigit:
						good = None
					lastDigit = y
			if good:
				lastValue = x
		print "Case #%d: %d"%(case, lastValue)
		case += 1 			
			
