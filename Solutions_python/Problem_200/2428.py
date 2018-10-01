def down(op,i):
	op[i] = chr(ord(op[i])-1)

for _ in range(int(input())):
	ip = input()
	if(len(ip) == 1):
		print("Case #{}: {}".format(_+1,ip))
		continue

	op = list(ip)
	i = 0
	while(i < (len(ip)-1)):
		if op[i] <= op[i+1]:
			i+=1
			continue

		down(op,i)
		j = i+1
		while j < len(op):
			op[j] = '9'
			j+=1

		if i != 0:
			i-=1
		else:
			i = 0

	print("Case #{}: {}".format(_+1,int(''.join(op))))



