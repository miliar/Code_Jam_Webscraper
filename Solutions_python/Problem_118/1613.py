import math
import sys,os

#3
#1 4
#10 120
#100 1000

def isPal(digits):
	if str(digits) == str(digits)[::-1]:
		return 1
	return 0

i=1
sqrtList = []

while i < 10000000:
	if isPal(i) == 1:
		if isPal(i*i) == 1:
			sqrtList.append(i)
	i += 1

#print sqrtList

file = open(sys.argv[1],'r')

file.readline()

case = 1

for line in file:
	if len(line)<2:
		continue
	print "Case #"+str(case)+": ",
	case += 1
	hits = 0

	
	low = int(line.split(' ')[0].strip())
	high = int(line.split(' ')[1].strip())

#	print low, high
	for num in sqrtList:
		if num*num >= low and num*num <= high:
#			print num, num*num
			hits += 1
	print hits
		
