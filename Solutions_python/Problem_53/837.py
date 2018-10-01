def snapper_chain(N,K):
	s = str(bin(K))
	s = s[2:]
	s = s[(len(s)-N):]
	if len(s) < N:
		return 'OFF'
	if '0' in s:
		return 'OFF'
	return 'ON'

if __name__ == '__main__':
	T = int(raw_input())
	for i in xrange(T):
		tmp = raw_input().split()
		N = int(tmp[0])
		K = int(tmp[1])
		print 'Case #'+str(i+1)+': '+snapper_chain(N,K)
