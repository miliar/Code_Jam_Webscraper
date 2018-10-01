def isPow2(x):
	if x==1:
		return True
	if x%2==1:
		return False
	return isPow2(x/2)

def mcd(x,y):
	while x>0:
		t=x
		x=y%x
		y=t
	return y

class Frac:
	def __init__(self,n,d):
		self.n=n
		self.d=d

	def simple(self):
		m=mcd(self.n,self.d)
		self.n=self.n/m
		self.d=self.d/m

	def __str__(self):
		return str(self.n)+'/'+str(self.d)


a=open('A-large.in')
b=open('out.txt','w')

cases=int(a.readline())

for case in range(cases):

	num=map(int,a.readline().split('/'));
	F=Frac(num[0],num[1])

	if F.d>0:
		F.simple()

	resp=0
	
	isValid=isPow2(F.d)

	cond=(not(F.n==0) or not(F.n==1 and F.d==1)) and isValid

	if not(isValid) or F.d<F.n:
		resp="impossible"

	while cond:

		F.d=F.d/2

		resp+=1
		if F.n>=F.d:
			break		
			
	b.write("Case #"+str(case+1)+": "+str(resp)+'\n')
b.close()
