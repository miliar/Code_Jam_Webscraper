t = int(input())
for i in range(t):
	str1,k = input().split();
	k = int(k)
	str1 = list(str1)
	count = 0;
	if(str1.count('-') == 0):
		print("Case #" + str(i+1) + ": " + str(count))
	else:
		n = 0
		while(n<=len(str1)-k):
			if(str1[n]=="-"):
				count = count + 1
				temp = k-1
				while(temp>=0):
					if(str1[n+temp] == "-"): 
						str1[n+temp] = "+"
					else:
						str1[n+temp] = "-"
					temp = temp -1
			if("-" not in str1):
				print("Case #" + str(i+1) + ": " + str(count))
				break;
			n = n + 1
		if(n > len(str1)-k):
			print("Case #" + str(i+1) + ": " + "IMPOSSIBLE")
