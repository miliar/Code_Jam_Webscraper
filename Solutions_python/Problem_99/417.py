def main():
	#t=int(raw_input())
	f=open("test","r")
	t=int(f.readline())
	for i in range(t):
		#a,b=raw_input().split()
		a,b=f.readline().split()
		a=int(a)
		b=int(b)
		n = b+2
		#p=raw_input().split()
		p=f.readline().split()
		pv=1
		expval=[]
		for j in range(len(p)):
			p[j] = float(p[j])
			pv*=p[j]
		expval+=[KeepTyping(a,b,p,pv)]
		expval+=BackSpace(a,b,p)
		expval+=[EnterRightAway(a,b,p)]
		print("Case #"+str(i+1)+": " +str(min(expval)))
		
def EnterRightAway(a,b,p):
	return b+2

def BackSpace(a,b,p):
	backList=[]
	for i in range(1,a):
		backList+=[GoBack(a,b,p,i)]
	return backList
		
def GoBack(a,b,p,i):
	pv=1
	for j in range(a-i):
		pv*=p[j]
	minsteps = 2*i+b-a+1
	maxsteps = minsteps + b+1
	return minsteps*pv + (1-pv)*maxsteps
	
		
def KeepTyping(a,b,p,pv):
	minsteps = b-a+1
	maxsteps = b+minsteps+1
	return (pv*minsteps + (1-pv)*maxsteps)
	

if __name__=='__main__':
	main()
	
