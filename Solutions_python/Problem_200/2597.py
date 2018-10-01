def asc(arr):
	i=0
	while i<len(arr)-1:
		if arr[i]>arr[i+1]:
			return False
		i+=1
	return True
for _ in range(int(input())):
	ans='Case #'+str(_+1)+': '
	n=input()
	n=list(n)
	if len(n)==1:
		print(ans+str(int(''.join(n))))
		continue
	while(not asc(n)):
		i=0
		while i<len(n)-1:
			if n[i]>n[i+1]:
				n[i]=str(int(n[i])-1)
				i+=1
				while i<len(n):
					n[i]='9'
					i+=1
			i+=1
	print(ans+str(int(''.join(n))))