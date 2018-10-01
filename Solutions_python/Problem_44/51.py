import sys

v=open(sys.argv[1],"r");
ot=open(sys.argv[2],"w");

z=v.readlines()
T=int(z[0])
cpos=1
for i in xrange(1,T+1):
	p=int(z[cpos])
	cpos+=1
	fly=[0,0,0,0,0,0]
	for j in xrange(0,p):
		q=map(int,z[cpos].split(" "))
		print q
		cpos+=1
		for k in xrange(0,6):
			fly[k]+=q[k]
	for k in xrange(0,6):
		fly[k]/=float(p)
	print fly
	if fly[3]**2+fly[4]**2+fly[5]**2==0:
		t=0
	else:
		t=-(fly[0]*fly[3]+fly[1]*fly[4]+fly[2]*fly[5])/float(fly[3]**2+fly[4]**2+fly[5]**2)
		if t<0:
			t=0
	p=(fly[3]*t+fly[0])**2+(fly[4]*t+fly[1])**2+(fly[5]*t+fly[2])**2
	p=p**.5
	ot.write("Case #%i: %.9f %.9f\n"%(i,p,t));
ot.close()

print cpos,len(z)
	
