from sys import stdin as f

def res_time(balance, rate, target):
	return (target - balance)/rate

T = int(f.readline())
for t in range(1, T + 1):
	C, F, X = map(float, f.readline().split())
	rate = 2.0
	balance = 0
	time = 0
	
	while True:
		res_time_waiting = res_time(balance, rate, X)
		res_time_investing = res_time(balance, rate, C) + res_time(0, rate + F, X)
		if res_time_waiting <= res_time_investing:
			print("Case #%d: %0.7f" % (t, time + res_time_waiting))
			break
		else:
			time = time + res_time(balance, rate, C)
			balance = 0
			rate = rate + F
		
	
