def GetCount(a,b):
	g={}
	count={}
	for i in range(a,b+1):
		k=str(i)
		l=[]
		for j in range(len(k)):
			l += [k[j]]
		k = int(''.join(map(str,l)))
		for j in range(len(l)):
			l.insert(0,l.pop())
			h=int(''.join(map(str,l)))
			if h > k and h<=b:
				if k in g.keys():
					if h not in g[k]:
						g[k] +=[h]
						count[k] +=1
				else:
					g[k] =[h]
					count[k]=1
	return sum(count.values())
			

def main():
	#f=open("test","r")
	#t=int(f.readline())
	t=int(raw_input())
	for i in range(t):
		limits = raw_input().split()
		limits = f.readline().split()
		a=int(limits[0])
		b=int(limits[1])
		count = GetCount(a,b)
		print("Case #"+str(i+1)+": "+str(count))
	
	
	return

if __name__=='__main__':
	main()
