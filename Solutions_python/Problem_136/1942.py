import fileinput
case = 0
for line in fileinput.input():
	line = line.strip()
	if fileinput.isfirstline():
		cases = int(line)
	else:
		case += 1
		production = 2.0
		time = 0.0
		farm_price, farm_prod, cookie_goal = [float(x) for x in line.split(" ")]
		while cookie_goal/production > (farm_price/production + cookie_goal/(farm_prod+production)):
			time += farm_price/production
			production += farm_prod
		time += cookie_goal/production
		print "Case #"+str(case)+": {:.7f}".format(time)


