fin = open("B.in", "r")
fout = open("B_.out","w")
lines = fin.readlines();
T = int(lines[0])
for c in range(1,T+1):
	lol = lines[c].split()
	L = int(lol[0])
	P = int(lol[1])
	C = int(lol[2])
	if L*C >= P:
		s = 'Case #'+str(c)+': 0\n'
		fout.write(s)
	else:
		ct=1
		aux=L*pow(C,2)
		while(aux<P):
			aux=aux*pow(C,pow(2,ct))
			ct=ct+1
		s = 'Case #'+str(c)+': '+str(ct)+'\n'
		fout.write(s)
	
