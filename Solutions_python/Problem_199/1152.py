t = int(input())
for i in range(0,t) :
	s = input()
	tmp = s.split()
	sign = list(tmp[0])
	size = int(tmp[1])
	#print("".join(sign), size)
	
	cursor = 0
	count = 0
	while cursor <= len(sign) - size :
		if sign[cursor] == "-":
			for n in range(0,size):
				if sign[cursor+n] == '-':
					sign[cursor+n] = '+'
				else :
					sign[cursor+n] = '-'
			count += 1
		cursor += 1
		#print("".join(sign), cursor, count)
	
	impossible = False
	for c in sign :
		if c == '-' :
			impossible = True
			
	if (impossible) :
		print("Case #", i+1, ": IMPOSSIBLE", sep="")
	else :
		print("Case #", i+1, ": ", count, sep="")