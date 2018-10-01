# happy face up
ncase = int(input())

def flip(mys,myk):
	ans = 0
	if mys[0] == "-":
		ans = 1
		for j in range(myk):
			if mys[j] == "+":
					mys[j] = "-"
			else:
					mys[j] = "+"
	return ans

def cut(mys):
	lenOfS = len(mys)
	j = 0
	while j < lenOfS:
		if mys[j] == "-":
			break
		else:
			j += 1
	return mys[j:]

for i in range(ncase):
	sk = input().split()
	s = list(sk[0])
	k = int(sk[1])
	#print(s)
	
	t = 0
	while len(s) >= k :
		t += flip(s,k)
		s = cut(s)
		#print(s)
	
	if len(s) != 0:
		print("Case #%d: IMPOSSIBLE"%(i+1))
	else:
		print("Case #%d: %d"%(i+1,t))