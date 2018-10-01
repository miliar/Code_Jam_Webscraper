t = int(input())

for ii in range(t):
	
	cakes,k = input().split()
	k = int(k)
	
	ch_cakes = [-1]
	for i in range(len(cakes)):
		if(cakes[i] == '+'):
			ch_cakes.append(0)

		else:
			ch_cakes.append(1)


	ctr = [0]
	flag = True

	for i in range(1, len(ch_cakes)):
		left = max(0,i-k)
		res = (ch_cakes[i]+ctr[i-1] - ctr[left])%2
		
		if(i+k <= len(ch_cakes)):
			ctr.append(ctr[i-1]+res)

		else:
			if(res == 1):
				flag = False
				break

			else:
				ctr.append(ctr[i-1])

	if(flag):
		print("Case #",ii+1,": ",ctr[-1],sep="")
	else:
		print("Case #",ii+1,": IMPOSSIBLE",sep="")




