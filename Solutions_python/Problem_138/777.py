
DEBUG=0
import random

def sa(A, B):
	A.sort()
	B.sort()
	if DEBUG:
		print A, B
	point=0
	for b in B:
		while A:
			a=A[0]
			A[0:1]=[]
			if a>b:
				point+=1
				break
		if A==[]:
			break
	return point
def sb(l, B):
	bp=filter(lambda x:x>l, B)
	if bp:
		element=min(bp)
	else:
		element=min(B)
	B.remove(element)
	if DEBUG:
		print 'element', element
	return element

def g(m, u, n):
	for x in range(n):
		r=random.choice(u)
		m.append(r)
		u.remove(r)

def TEST():
	N=5
	U=range(N*2)
	A=[]
	B=[]
	g(A, U, N)
	g(B, U, N)

	print 'A', A
	print 'B', B
	Solve(A, B, N)

def Solve(A, B, N):
	for t in range(1):
		CA=list(A)
		CB=list(B)
		strategy_a=[]
		g(strategy_a, CA, N) 
		if DEBUG:
			print strategy_a
		point=0
		for e in strategy_a:
			re=sb(e, CB)
			if re<e:
				point+=1
		s2=point
	s1=sa(A,B)
	return s1, s2

filename='D-large-0'
f=file('%s.in'%filename, 'r')
of=file('%s.out'%filename, 'w')
T=int(f.readline())
for t in range(T):
	N=int(f.readline())
	la=f.readline().split(' ')
	la=[float(x) for x in la]
	lb=f.readline().split(' ')
	lb=[float(x) for x in lb]
	s1,s2=Solve(la, lb, N)
	of.write( "Case #%d: %d %d\n"%(t+1, s1,s2))
