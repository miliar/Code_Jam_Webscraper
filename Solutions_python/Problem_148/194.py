def ProcessOne():
	inp = raw_input().split()
	N = int(inp[0])
	X = int(inp[1])

	S = map(lambda x : int(x), raw_input().split())
	S.sort()

	res = N
	while len(S) != 0:
		tester = S[0]
		S = S[1:]

		k = len(S) - 1
		success = False
		while k >= 0 and not success:
			if tester + S[k] <= X:
				del S[k]
				res -= 1
				success = True
			k -= 1
		
		if not success:
			S = [tester] + S
			break

	print ("Case #%(id)s: %(res)s" % {"id" : i+1, "res" : res})


T = int(raw_input())

for i in range(T):
	ProcessOne()




