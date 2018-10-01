#!/usr/bin/python3

t = int(input());
for ti in range (1, t+1):
	stalls, users = [int(s) for s in input().strip().split(" ")]
	#print(stalls);
	#print(users);
	
	dist = dict();
	dist[stalls] = 1;
	
	while(users > 1):
		n = max(dist.keys());
		if(n%2 == 0):
			n1 = (n-2)//2
			n2 = n//2
		else:
			n1 = (n-1)//2
			n2 = (n-1)//2
		num = min(users-1, dist[n]);
		dist[n] -= num;
		users -= num;
		if n1 not in dist:
			dist[n1] = 0
		dist[n1] += num;
		if n2 not in dist:
			dist[n2] = 0
		dist[n2] += num;
		if(dist[n] == 0):
			del dist[n]
		
		#print(dist)
	n = max(dist.keys())
	if(n%2 == 0):
		low = (n-2)//2;
		up = n//2;
	else:
		low = (n-1)//2;
		up = (n-1)//2;
		
	print("Case #{}: {} {}".format(ti, up, low));
