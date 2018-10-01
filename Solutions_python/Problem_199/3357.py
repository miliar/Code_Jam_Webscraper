def calc(s,k):
	ans = 0
	list = []
	for i in range(len(s)):
		if s[i]=='+':
			list.append(1)
		else:
			list.append(0)
	for i in range(len(list)):
		if list[i]==0:
			ans+=1
			#print i
			if i+k<=len(list):
				for j in range(i,i+k):
					list[j] = 1-list[j]
			else:
				return "IMPOSSIBLE"
	return ans
	


f = open("test.txt")
#f2 = open("out.txt","w")
t = int(f.readline())

for i in range(1,t+1):
	x = (f.readline())
	x = x.split()
	#print x
	#f2.write
	print("Case #"+str(i)+": "+str(calc((x[0]),int(x[1]))))	
