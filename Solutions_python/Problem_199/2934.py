def flip(s, startWith, k):
	for i in range(startWith, startWith+k):
		if s[i] == "+":
			s[i] = "-"
		else:
			s[i] = "+"

t = int(raw_input())

for i in range(1,t+1):
	inputList = raw_input()
	p = len(inputList)-1
	while p>=0:
		if inputList[p]==" ":
			break
		p-=1
	s = list(inputList[:p])
	k = int(inputList[p+1:])

	startWith = 0
	endWith = len(s)-1
	f = 0

	while ((endWith-startWith+1) > k):
		if s[startWith] == "-":
			flip(s, startWith, k)
			f+=1
		startWith+=1
		
		if (endWith-startWith+1) > k:
			if s[endWith] == "-":
				flip(s, endWith-k+1, k)
				f+=1
			endWith-=1

	for j in range(startWith,endWith):
		if s[j]==s[j+1]:
			pass
		else:
			print "Case #{}: {}".format(i, "IMPOSSIBLE")
			break 
		if j+1 == endWith:
			if s[j] =="+":
				print "Case #{}: {}".format(i, f)
			else:
				print "Case #{}: {}".format(i, f+1)
