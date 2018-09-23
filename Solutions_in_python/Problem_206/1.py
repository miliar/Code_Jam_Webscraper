T = int(raw_input())

for test in xrange(1,T+1):
	D, N = map(int, raw_input().split())
	K = [] 
	for _ in xrange(N):
		k, s = map(int, raw_input().split())
		K.append((k,s))
	K.append((D, 0))
	K.sort()
	S = [ s for _,s in K]
	K = [ k for k,s in K]
	ans = 0.
	try :
		while len(K)>1 :
			t, ix = 10**12, 0
			for i in xrange(len(K)-1):
				if S[i]>S[i+1] : 
					tmp = (1.*(K[i+1]-K[i]))/(S[i]-S[i+1])
					if tmp<t : t, ix = tmp, i
			K.remove(K[ix])
			S.remove(S[ix])
			K = [ min(D,k + t*s) for k,s in zip(K,S) ]
			ans += t
		print "Case #%d: %.6f"%(test, 1.*D/ans)
	except : print "Error : ", D, N, K, ans, t
 
