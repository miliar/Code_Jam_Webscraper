for t in range(int(input())):
	n = list(input())[::-1]
	for i in range(0,len(n)-1):
		if n[i] < n[i+1]:
			n[i+1] = chr(ord(n[i+1])-1)
			for j in range(0,i+1):
				n[j] = '9'
	print("Case #{}: {}".format(t+1,int(''.join(n[::-1]))))