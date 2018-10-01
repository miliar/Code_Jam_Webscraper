import sys

counter = 0
number = 0

def isTidy(num):
	len_num = len(str(abs(num)))
	prev = -1
	#print "num is ",num
	while(len_num > 0):
		dig = num % pow(10,1)
		#print dig
		if ((dig > prev) and (prev != -1)):
			return False
		prev = dig
		num = num / 10
		len_num -= 1
	return True

def makeithdigit9(num,i):
	len_num = len(str(abs(num)))
	index = 1
	prefix = num/(pow(10,i))
	suffix = num%(pow(10,i-1))
	digit = 9
	if(suffix != 0):
		ans = str(prefix-1) + str(digit) + str(suffix)
	else:
		ans = str(prefix-1) + str(digit)
	#print "Making ith digigt 9", i, num, prefix-1, digit, suffix, ans
	return int(ans)

with open(sys.argv[1],"r") as in_file:
	for line in in_file:
		if counter == 0:
			number = line
		else:
			testnumber = int(line)
			#print testnumber
			#counter = testnumber
			i = 1
			while (isTidy(testnumber)== False):
				#print testnumber
				testnumber = makeithdigit9(testnumber,i)
				i += 1

			print "Case #"+str(counter)+": "+str(testnumber)
		counter += 1