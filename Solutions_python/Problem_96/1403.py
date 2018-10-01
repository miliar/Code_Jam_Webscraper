t = input()
for i in range(t):
	inp = raw_input().split()
	n = int(inp[0])
	s = int(inp[1])
	min = int(inp[2])
	count=0
	ans = 0
	for j in inp[3:]:
		curr = int(j)
		if curr/3 >=min:
			ans+=1
		elif curr==0:
			continue
		elif curr/3 == min-1 and curr%3>0:
			ans+=1
		elif curr/3 >= min-1 and curr%3==0 and count<s:
			ans+=1
			count+=1
		elif curr/3 == min-2 and curr%3==2 and count<s:
			ans+=1
			count+=1
	print "Case #"+str(i+1)+":",ans
