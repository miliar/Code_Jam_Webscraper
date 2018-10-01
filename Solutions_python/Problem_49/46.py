


inf = float("infinity")

def sprrad(p1, p2):
	dx = p1['x']-p2['x']
	dy = p1['y']-p2['y']
	return ((dx**2 + dy**2)**.5 + p1['r'] + p2['r']) / 2.0


C = int(input())

for x in range(1,C+1):
	N = int(input())
	plants = []
	for p in range(N):
		X,Y,R = [int(w) for w in input().split()]
		plants += [ {'x':X, 'y':Y, 'r':R} ]
	
	#only 3 plants
	
	best = inf
	
	if len(plants)==1:
		best = plants[0]['r']
	elif len(plants)==2:
		best = max(plants[0]['r'],plants[1]['r'])
	elif len(plants)==3:
		b0 = max(plants[0]['r'], sprrad(plants[1],plants[2]) )
		b1 = max(plants[1]['r'], sprrad(plants[2],plants[0]) )
		b2 = max(plants[2]['r'], sprrad(plants[0],plants[1]) )
		best = min(b0,b1,b2)
	
	R = best
	print("Case #"+str(x)+": "+str(R))
































