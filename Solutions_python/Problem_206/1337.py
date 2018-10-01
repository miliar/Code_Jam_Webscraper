for i in range (int(input())):
	s = []
	k = []
	t = []
	D,N = map(int, input().split())
	for temp in range(N):
		temp1, temp2 = map(int,input().split())
		k.append(temp1)
		s.append(temp2)
		t.append(float(D-temp1)/temp2)
	time = max(t)
	print("Case #%d: %.6f"%(i+1, round( float(D/time), 6 , )))
