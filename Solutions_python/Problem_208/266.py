f = open("ponyExpressSmall.in", "r")
new_file = open("ponyExpressSmallSol", "w")
t = int(f.readline())

def pony_express(n, eisis, ds):
	memo = {}
	def dp_sol(horse_dist_left, horse_speed, current_city):
		new_horse_dist, new_horse_speed = eisis[current_city]
		dist = ds[current_city]
		if horse_dist_left >= dist:
			if new_horse_dist < dist:
				firstadd = float(dist)/horse_speed
				secondadd = 100000000000000
			else:
				firstadd = float(dist)/horse_speed
				secondadd = float(dist)/new_horse_speed
		else:
			if new_horse_dist >= dist:
				secondadd = float(dist)/new_horse_speed
				firstadd = 100000000000000
		if current_city == (n-2):
			if horse_dist_left >= dist:
				if new_horse_dist < dist:
					return float(dist)/horse_speed
				else:
				
					return min(float(dist)/horse_speed, float(dist)/new_horse_speed)
			else:
				if new_horse_dist >= dist:
					 return float(dist)/new_horse_speed
				else:
					return 10000000000000000
		if (horse_dist_left-dist, horse_speed, current_city+1) in memo:
			first_value = memo[(horse_dist_left-dist, horse_speed, current_city+1)]
		else: 
			first_value = dp_sol(horse_dist_left-dist, horse_speed, current_city+1)
			memo[(horse_dist_left-dist, horse_speed, current_city+1)] = first_value
		if (new_horse_dist-dist, new_horse_speed, current_city+1) in memo:
			second_value = memo[(new_horse_dist-dist, new_horse_speed, current_city+1)]
		else: 
			second_value = dp_sol(new_horse_dist-dist, new_horse_speed, current_city+1)
			memo[(new_horse_dist-dist, new_horse_speed, current_city+1)] = second_value
		return min(firstadd + first_value, secondadd + second_value)

	return dp_sol(eisis[0][0], eisis[0][1], 0)

for i in range(1,t+1):
	n, q = [int(x) for x in f.readline().split(' ')]
	eisis = []
	ds = []
	for j in range(n):
		ei, si = [int(x) for x in f.readline().split(' ')]
		eisis.append((ei,si))
	for k in range(n-1):
		distances = [int(x) for x in f.readline().split(' ')]
		ds.append(distances[k+1])
	nothing = f.readline()
	nothing = f.readline()
	new_file.write("Case #"+str(i)+ ": "+str(pony_express(n,eisis, ds))+"\n")