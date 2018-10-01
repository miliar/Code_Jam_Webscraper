#! /usr/bin/env python

input = open("/Users/benzax/code_jam/input.txt",'r')

output = open("/Users/benzax/code_jam/output.txt",'w')

# 0123456789012345678
# welcome to code jam

N = int(input.readline())

for i in xrange(1,N+1):
	line = input.readline()

	count = [0]*19
	
	for index in range(0, len(line)):
		if line[index] == 'w' :
			count[0] = (count[0] + 1)%10000
		if line[index] == 'e' :
			count[1] = (count[1] + count[0])%10000
			count[6] = (count[6] + count[5])%10000
			count[14] = (count[14] + count[13])%10000
		if line[index] == 'l' :
			count[2] = (count[2] + count[1])%10000
		if line[index] == 'c' :
			count[3] = (count[3] + count[2])%10000
			count[11] = (count[11] + count[10])%10000
		if line[index] == 'o' :
			count[4] = (count[4] + count[3])%10000
			count[9] = (count[9] + count[8])%10000
			count[12] = (count[12] + count[11])%10000
		if line[index] == 'm' :
			count[5] = (count[5] + count[4])%10000
			count[18] = (count[18] + count[17])%10000
		if line[index] == ' ' :
			count[7] = (count[7] + count[6])%10000
			count[10] = (count[10] + count[9])%10000
			count[15] = (count[15] + count[14])%10000
		if line[index] == 't' :
			count[8] = (count[8] + count[7])%10000
		if line[index] == 'd' :
			count[13] = (count[13] + count[12])%10000
		if line[index] == 'j' :
			count[16] = (count[16] + count[15])%10000
		if line[index] == 'a' :
			count[17] = (count[17] + count[16])%10000
			
			
	num = count[18]
	
	s = ""
	if num < 10:
			s = "Case #" + str(i) + ": 000" + str(num) + "\n"
	elif num < 100:
			s = "Case #" + str(i) + ": 00" + str(num) + "\n"
	elif num < 1000:
			s = "Case #" + str(i) + ": 0" + str(num) + "\n"
	else:
			s = "Case #" + str(i) + ": " + str(num) + "\n"
	output.write(s)
	
