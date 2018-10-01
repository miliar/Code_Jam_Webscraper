def cookies():
	user_input = raw_input("")
	cookies_per_farm, rate_increase, target = user_input.split(" ")
	cookies_per_farm = float(cookies_per_farm)
	rate_increase = float(rate_increase)
	target = float(target)
	
	cookies = 0
	cookie_rate = 2
	time = 0

	
	while True:
		time_remaining = (target - cookies) / cookie_rate
		buy_farm_time = (cookies_per_farm - cookies) / cookie_rate
		added_farm_time = target / (cookie_rate + rate_increase)
		
		increase_rate_time = buy_farm_time + added_farm_time
		if time_remaining < increase_rate_time:
			return time + time_remaining
		else:
			cookies = 0
			time += buy_farm_time
			cookie_rate += rate_increase
	return time
		
	


def main():
	tests = int(raw_input(""))
	for i in range(tests):
		time = cookies()
		print("Case #{0}: {1}".format((i+1), time))

if __name__ == "__main__":
	main()