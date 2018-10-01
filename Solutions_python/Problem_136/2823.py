fx = open("temp.txt","w")
n = int(raw_input());
for z in range(1,n+1):
	k = raw_input();
	k = k.split(" ");
	C = float(k[0])
	F = float(k[1])
	X = float(k[2])
	cookie = 0.0
	f = 2
	time = 0.0
	while(1):
		t1 = X/f;
		t2 = C/f + X/(f+F);
		if(t1>t2):
			time = time + C/f
			f = f+F
		else:
			time = time +X/f
			break;
	fx.write("Case #"+str(z)+": "+str(time)+"\n")
fx.close()		
		
