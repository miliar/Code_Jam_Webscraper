T = input()
f = open("Boutput.txt","w")
Z = 1
while Z<=T:
	C,F,X = [float(z) for z in raw_input().strip().split()]
	R = 2.000000
	final_t = 0
	while (((C/R)+(X/(R+F)))<(X/R)):
		final_t += C/R
		R += F
	final_t += X/R
	f.write("Case #"+str(Z)+": %.7f\n"%final_t)
	Z+=1
f.close()
	
