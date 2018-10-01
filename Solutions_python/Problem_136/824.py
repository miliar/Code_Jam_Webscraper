

def entre():
	n=int(raw_input())
	inpute=[]
	outpute=[[] for i in range(n)]
	for i in range(n):
		s=raw_input()
		s=s.split()
		tt=[]
		for j in s:
			tt.append(float(j))
		inpute.append(tt)
	return inpute,outpute

E,S=entre()

nb=0
for T in E:
	nb+=1
	r=0
	p=2.0
	C=T[0]
	F=T[1]
	X=T[2]
	while ((C/p)+(X/(p+F)))<(X/p):
		r+=C/p
		p+=F
	r+=X/p
	print("Case #"+str(nb)+": "+str("%.7f" % round(r,7)))