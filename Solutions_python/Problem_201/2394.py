class SET(object):
	def __init__(self):
		self.l = []
	def add(self,x):
		self.l.append(x)
		self.l.sort()
		return
	def getlength(self):
		return len(self.l)
	def getelement(self,i):
		return self.l[i]
	def getLR(self):
		L,R = self.l[0],self.l[1]
		mini = R-L
		for i in range(1,self.getlength()-1):
			diff = self.l[i+1] - self.l[i]
			if diff > mini:
				mini = diff
				L,R = self.l[i],self.l[i+1]
		return L,R
def getLS(L,S):
	return S-L-1
def getRS(R,S):
	return R-S-1

t= int(input())

for a0 in range(t):
	n,k = map(int,input().split())
	if n == k:
		print("Case #{}: 0 0".format(a0+1))
		continue
	s = SET()
	s.add(0)
	s.add(n+1)
	for i in range(k):
		L,R = s.getLR()
		diff = R-L
		S = L+(diff//2)
		#print("L:{} R:{} S:{}".format(L,R,S))
		s.add(S)
	#print("L:{} R:{} S:{}".format(L,R,S))
	LS = getLS(L,S)
	RS = getRS(R,S)
	y = max(LS,RS)
	z = min(LS,RS)
	print("Case #{}: {} {}".format(a0+1,y,z))

