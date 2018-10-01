import fileinput
import sys
import math

upperlimit = int("1"+"0"*14)
maxcase = 0
currentcase = 0
fairsqdb = []

def ispali(s):
	length = len(s)
	for i in xrange(0,length/2):
		if s[i] != s[(length-1)- i]: return False
	return True

def nextpali(s):
	length = len(s)
	middle = ""

	if length == 1:
		newpali = str(int(s) + 1)
		if len(newpali) > 1:
			return "11"
		else:
			return newpali

	if length % 2 == 0:
		head = s[0:length/2]
		tail = s[length/2:][::-1]

		if int(head) <= int(tail):
			newhead = str(int(head) + 1)
			if len(newhead) > len(head):
				head = newhead[0:-1]
				middle = newhead[-1]
			else:
				head = newhead
	else:
		head = s[0:(length-1)/2]
		tail = s[(length+1)/2:][::-1]
		if int(head) <= int(tail):
			fakehead = s[0:(length+1)/2]
			newfakehead = str(int(fakehead) + 1)

			if len(newfakehead) > len(fakehead):
				head = newfakehead[0:-1]
			else:
				head = newfakehead[0:-1]
				middle = newfakehead[-1]


	return head + middle + head[::-1]


i = "0"
while True:
	i = nextpali(i)
	square = int(i)**2
	if (square > upperlimit):
		break
	elif ispali(str(square)):
		fairsqdb.append(square)


for line in fileinput.input():
	if fileinput.isfirstline():
		maxcase = line.strip()
		continue

	currentcase += 1
	(strA, strB) = line.split()
	fairsquarecount = 0

	sys.stdout.write("Case #"+str(currentcase)+": ")	
	sys.stdout.flush()

	A = int(strA)
	expA = len(strA)-1
	B = int(strB)
	expB = len(strB)-1

	print len(filter(lambda x: x >= A and x <= B, fairsqdb))

	# n = int(math.ceil(math.sqrt(A)))
	# strN = str(n)
	# if (not ispali(strN)):
	# 	strN = nextpali(strN)

	# while True:
	# 	expN = len(strN) - 1

	# 	if (expN*2 > expB):
	# 		break

	# 	square = int(strN)**2
	# 	if square > B:
	# 		break
	# 	elif ispali(str(square)):
	# 		fairsquarecount += 1

	# 	strN = nextpali(strN)


	# print fairsquarecount
	
	if maxcase == currentcase:
		break
