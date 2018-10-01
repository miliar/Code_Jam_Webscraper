n=int(input())
for tc in range(n):
	k=input()[::-1]
	kk=[]
	for i in k:
		kk.append(i)
	for i in range(len(k)-1):
		if ord(kk[i])<ord(kk[i+1]):
			kk[i+1]=chr(ord(kk[i+1])-1)
			kk[i]='9'
			for j in range(i):
				kk[j]='9'
	print("Case #%d: %d"%(tc+1,int("".join(kk)[::-1])))
