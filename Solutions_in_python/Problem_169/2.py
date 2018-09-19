for tc in range(1,int(input())+1):
	l=input().split()
	N=int(l[0])
	V=float(l[1])
	X=float(l[2])
	d=[]
	for n in range(N):
		dt=[float(x) for x in input().split()]
		d.append(dt)
	if (N==1 and X!=d[0][1]) or (N==2 and max(d[0][1],d[1][1])<X) or (N==2 and d[0][1]==d[1][1] and d[0][1]!=X) or (N==2 and d[0][1]>X and d[1][1]>X):
		print("Case #{_tc}: IMPOSSIBLE".format(_tc=tc))
		continue
	if N==1 and X==d[0][1]:
		sol = V/d[0][0]
	elif N==2 and d[0][1]==d[1][1] and d[0][1]==X:
		sol = V/(d[0][0]+d[1][0])
	else:
		v0 = V*(X-d[1][1])/(d[0][1]-d[1][1])
		v1 = V-v0
		t0 = v0/d[0][0]
		t1 = v1/d[1][0]
		sol = max(t0,t1)
	print("Case #{_tc}: {_sol}".format(_tc=tc,_sol=sol))
