from math import pi
filename = 'A-large.in'
f = open(filename,'r')

T = int(f.readline())
for t in range(1,T+1):
	print "Case #%d:" % t ,
	N, K = map(int,f.readline().split())
	RH = [0]*N
	for i in range(N):
		RH[i] = map(int,f.readline().split())
	RH.sort()
	ans = 0
	for i in range(K-1,N):
		if K == 1:
			ans = max(ans,pi*(RH[i][0]**2+2*RH[i][0]*RH[i][1]))
		else:
			maxelem = RH[i]
			rh = RH[:i]
			rh.sort(key=lambda x: x[0]*x[1], reverse=True)
			a = maxelem[0]*maxelem[1]
			for j in rh[:K-1]:
				a += j[0]*j[1]
			ans = max(ans,pi*(maxelem[0]**2+2*a))
	print "%.12f" % ans
