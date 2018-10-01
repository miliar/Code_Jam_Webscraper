T = int(raw_input())
for i in range(T):
	N = '0' + raw_input()
	k = len(N)
	while ''.join(sorted(N)) != N:
		while ''.join(sorted(N[:k])) != N[:k]:
			k -= 1
		N = str(int(N[:k]) - 1) + '9'*(len(N)-k)
	print("Case #%d: %d" % (i+1, int(N)))