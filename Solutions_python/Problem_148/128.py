T = int(input())
for I in range(1, T+1):
	A, B = input().split(" ")
	N, X = int(A), int(B)
	s = input().split(" ")
	if len(s) % 2 != 0:
		s.append(0)
	S = [0]*len(s)
	for i in range(0, len(s)):
		S[i] = int(s[i])
	
	S.sort()
	
	bin = 0
	while (len(S) > 0):
		tmp = 0
		while tmp < len(S) and S[len(S)-1] + S[tmp] <= X:
			tmp += 1
		
		if (tmp > 0):
			S.pop(tmp-1)
		if (len(S) > 0):
			S.pop()
		bin += 1
	
	#print()
	result = bin
	
	print("Case #%d: %s" % (I,result))
