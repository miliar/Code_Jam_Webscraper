def flip(S,i,k):
	for x in range(i-k+1,i+1):
		S[x] = not S[x]

for _ in range(int(input())):
	ip = input().split()
	S = [x == '+' for x in ip[0]]
	#print(S)
	k = int(ip[1])
	del(ip)

	i = len(S) - 1
	nFlips = 0
	while i-k+1 >= 0:
		if S[i]:
			i-=1
			continue

		flip(S,i,k)
		nFlips+=1
		i-=1

	#print("lalx : ",S)
	if S.count(True) != len(S):
		nFlips = "IMPOSSIBLE"

	print("Case #{}: {}".format(_+1,nFlips))