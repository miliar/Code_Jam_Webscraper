ins = open( "B-large.in", "r" )
input = []
for line in ins:
    input.append( line.strip() )

ins.close()

numCases = input[0]
for i in range(1,int(numCases)+1):
	params = input[i].split(" ")
	cost = float(params[0])
	current_rate = 2.0
	upgrade_rate = float(params[1])
	win = float(params[2])

	total_time = 0.0
	current_cookies = 0.0

	start = True
	while start or upgrade < dont_upgrade:
		upgrade = cost/current_rate + win/(current_rate+upgrade_rate)
		dont_upgrade = win/current_rate
		if(upgrade < dont_upgrade):
			total_time = total_time + cost/current_rate
			current_rate = current_rate + upgrade_rate

		else:
			total_time = total_time + win/current_rate
		start=False
	
	print 'Case #'+str(i)+': ' + str(total_time)