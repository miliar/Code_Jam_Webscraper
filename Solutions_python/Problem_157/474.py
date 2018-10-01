m={
('i','j'):(1,'k'),
('j','k'):(1,'i'),
('k','i'):(1,'j'),
('j','i'):(-1,'k'),
('k','j'):(-1,'i'),
('i','k'):(-1,'j'),
}
C={}
def r(S):
	if len(S)<=1:
		return (1,S)
	if S not in C:
		s1,q1=r(S[:len(S)//2])
		s2,q2=r(S[len(S)//2:])
		if q1==q2=='':
			s,q=1,''
		elif q1==''or q2=='':
			s,q=1,q1+q2
		else:
			s,q=m.get((q1,q2),(-1,''))
		C[S]=(s*s1*s2,q)
	return C[S]
def sol():
	_,X=map(int,raw_input().split())
	S=raw_input()
	S=S*X
	if r(S)==(-1,''):
		for i in range(1,len(S)):
			if r(S[:i])==(1,'i'):
				for j in range(i+1,len(S)+1):
					if r(S[i:j])!=(1,'j'):
						continue
					if r(S[j:])==(1,'k'):
						return'Case #%d: YES'%(t+1)
	return'Case #%d: NO'%(t+1)
for t in range(input()):
	print sol()