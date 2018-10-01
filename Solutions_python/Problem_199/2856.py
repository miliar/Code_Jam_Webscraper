file = open("input.in","r")
count = file.readline()
output = open("output.txt","w")
for k, line in enumerate(file):
	st = line.split()
	s = st[0]
	val = int(st[1])
	count =0
	a =0
	lis = list(s)
	res = ''
	if lis.count('+') == len(lis):
		res = '0'
	while lis.count('+') != len(lis):
		if (a+val) > len(lis):
			res = "IMPOSSIBLE"
			break
		if lis[a] == '+':
			a +=1
			continue
		else:
			count +=1
			for i in range(a,(a+val)):
				if lis[i] == '+':
					lis[i] = '-'
				else:
					lis[i] = '+'
			a +=1
			res = str(count)
	output.write("Case #" + str(k+1) +": " + res + "\n")
output.close()