f = open("B-large.in")

L = int(f.readline().strip())

for i in range(L):
	C, F, X = map(float, f.readline().strip().split())

	P = 2
	T = 0
	Tmax = X/P	

	while(1):		
		if(T + C/P + X/(P+F) < Tmax):
			T += C/P
			P += F
			Tmax = T + X/P
		
		else: break
 
	print "Case #{}: {}".format(i+1, Tmax)


