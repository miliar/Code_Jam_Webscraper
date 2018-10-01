baca = open("A-large.in","r")
tulis = open("output.txt","w")
n = int(baca.readline())
for k in range(n):
	ans = 0
	s = baca.readline().split(" ")
	m = int(s[1])
	s = s[0]
	lst = []
	for i in s: lst.append(i)
	for i in range(len(lst)):
		if (lst[i] == "-" and len(lst)-i < m) :
			ans = -1
			break
		elif (lst[i] == "-") :
			ans += 1
			for j in range(m) : 
				if (lst[i+j] == "-") : lst[i+j] = "+"
				else : lst[i+j] = "-"
	if (ans == -1) : ans = "IMPOSSIBLE"
	tulis.write("Case #"+str(k+1)+": "+str(ans)+"\n")