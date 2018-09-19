t = int(raw_input())
k = 1
while t>0:
	speed = 2.00000;cookies = 0.00000;time = 0.00000;ans = 0.00000
	time1 = 0.00000;time2 = 0.00000;speed0 = 0.00000
	C, F, X = map(float, raw_input().split(" "))
	l = str(k)
	if X < C:
		ans = X/speed
		print('Case #'+l+": %.7f" % ans)
	else:
		while cookies < X:
			#if farm not purchased
			time1 = X/speed
			#if farm is purchased
			speed0 = speed + F
			time2 = C/speed + X/speed0
			#check which time is less
			if time1 > time2: #purchase the farm
				time += (C - cookies)/speed
				speed = speed0
				cookies = 0
			else: #go without purchasing farm
				time += time1
				cookies = X
		print('Case #'+l+": %.7f" % time)
 
	k += 1
	t -= 1