t = int(input(''))
cc = 0
while True:
	t-=1
	if t < 0:
		break
	cc += 1
	inp = input('')
	s = [float(p) for p in inp.split(' ')]
	
	c = s[0]
	f = s[1]
	x = s[2]
	
	min_time = float( x / 2.0)
	i = 0
	leftover = float(0)
	current_time = float(0)
	while True:
		current_time = current_time + (c/(2 + i*f))
		leftover = x/(2 + (i + 1)*f)
		if current_time + leftover < min_time:
			min_time = current_time + leftover
			i = i+1
		else:
			break

	print("Case #"+ str(cc) +":", "%.7f" % min_time)