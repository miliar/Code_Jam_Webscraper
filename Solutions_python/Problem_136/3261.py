
T = int(raw_input())

for i in range(T):

	C,F,X = map(float,raw_input().split())

	rate = 2
	time = 0

	while True:
		if X/rate < C/rate:
			time += X/rate
			break

		time += C/rate

		if X/(rate+F) < (X-C)/rate:
			rate+=F
		else:
			time+=(X-C)/rate
			break

	print("Case #"+str(i+1)+": "+str(time))

