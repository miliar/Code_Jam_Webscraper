def search(cost,farm,goal):
	time = 0.0
	speed = 2.0
	while time + goal / speed > time  + goal / (speed + farm) + cost / speed:
		time += cost / speed
		speed += farm
	return str(time + goal / speed)
# def search(speed,cost,farm,goal,elapsed):
# 	t = cost / speed + search(speed + farm,cost,farm,goal) + elapsed
# 	if goal / speed > t:
# 		return t
# 	return t + goal
with open("B--small-attempt0.in") as f:
	with open("result.txt","w") as out:
		n = int(f.readline().strip())
		for i in range(n):
			s = f.readline().strip().split()
			out.write("Case #%d: %s\n" % (i + 1,str(search(float(s[0]),float(s[1]),float(s[2])))))