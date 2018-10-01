text = open("B-large.in.txt", "r")
i = int(text.readline())
for j in range(1,i+1):
	total_time = 0
	inputs = map(float, text.readline().split(' '))
	C = inputs[0]
	F = inputs[1]
	X = inputs[2]
	f = 2
	while (X/f > (C/f+X/(f+F))):
		total_time = total_time + C/f
		f = f + F
	total_time = total_time + X/f
	print('Case #'+str(j)+': '+'%.7f' % total_time)