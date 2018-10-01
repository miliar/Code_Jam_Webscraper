f = open("in.txt",'r')

T = int(f.readline())
for t in range(T):
	l = f.readline().split()
	S = []
	for char in l[0]:
		S.append(char)
	K = int(l[1])	
	num = 0
	for i in range(len(S)-K+1):
		if S[i] != '+':
			for j in range(i,i+K):
				if S[j] == '+':
					S[j] = '-'
				else:
					S[j] = '+'
			num = num + 1
	good = True
	for i in range(len(S)):
		if S[i] == '-':
			good = False
	if good:
		print("Case #" + str(t+1) + ": " + str(num))
	else:
		print("Case #" + str(t+1) + ": IMPOSSIBLE")
	
