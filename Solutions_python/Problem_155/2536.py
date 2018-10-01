
cases = input()
case = 1
for i in range(cases):
	max,aud = raw_input().split(" ")
	result = 0
	init = 0
	count = 0
	for num in aud:
		if init >= count:
			init += int(num)
		else:
			result += (count-init)
			init +=(count-init)+int(num)
		count+=1
	print "Case #"+str(case)+": "+str(result)
	case+=1
