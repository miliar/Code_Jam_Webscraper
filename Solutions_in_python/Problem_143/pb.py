T=int(raw_input())
for i in range(T):
	S=str(raw_input())
	#print S
	A,B,K=S.split()
	A=int(A)
	B=int(B)
	K=int(K)
	cnt=0
	for j in range(A):
		for k in range(B):
			if (j & k < K):
				cnt=cnt+1
	print "Case #" + str(i+1) + ": " + str(cnt)
