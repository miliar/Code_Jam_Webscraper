t=int(input())
for ij in range(1,t+1):
	n,r,o,y,g,b,v=[int(s) for s in input().split(" ")]
	colours=[r,o,y,g,b,v]
	if(2*max(r,o,y,g,b,v)>n):
		print("Case #{}: IMPOSSIBLE".format(ij, n, r))
	elif(r==max(r,o,y,g,b,v)):
		ans=[]		
		for i in range(1,r+1):
			ans.append('R')
		m=0
		for i in range(1,y+1):
			ans.insert(m,'Y')
			m+=2
		m=1
		for i in range (1,b+1):
			ans.insert(len(ans)-m,'B')
			m+=2
				
		print("Case #{}: {}".format(ij, ''.join(ans)))
	elif(y==max(r,o,y,g,b,v)):
		ans=[]		
		for i in range(1,y+1):
			ans.append('Y')
		m=0
		for i in range(1,b+1):
			ans.insert(m,'B')
			m+=2
		m=1
		for i in range (1,r+1):
			ans.insert(len(ans)-m,'R')
			m+=2		
		print("Case #{}: {}".format(ij, ''.join(ans)))
	elif(b==max(r,o,y,g,b,v)):
		ans=[]		
		for i in range(1,b+1):
			ans.append('B')
		m=0
		for i in range(1,y+1):
			ans.insert(m,'Y')
			m=m+2
		m=1		
		for i in range (1,r+1):
			ans.insert(len(ans)-m,'R')
			m=m+2		
		print("Case #{}: {}".format(ij, ''.join(ans)))
	elif(y==max(r,o,y,g,b,v) and r>=b):
		ans=[]		
		for i in range(1,b+1):
			ans.append('B')
		m=0
		for i in range(1,r+1):
			ans.insert(m,'R')
			m+=2
		m=1
		for i in range (1,y+1):
			ans.insert(len(ans)-m,'Y')
			m+=2		
		print("4Case #{}: {}".format(ij,''.join(ans)))
	elif(b==max(r,o,y,g,b,v) and r>=y):
		ans=[]		
		for i in range(1,y+1):
			ans.append('Y')
		m=0
		for i in range(1,r+1):
			ans.insert(m,'R')
			m+=2
		m=1
		for i in range (1,b+1):
			ans.insert(len(ans)-m,'B')
			m+=2		
		print("5Case #{}: {}".format(ij,''.join(ans)))	
	elif(r==max(r,o,y,g,b,v) and b>=y):
		ans=[]		
		for i in range(1,y+1):
			ans.append('Y')
		m=0
		for i in range(1,b+1):
			ans.insert(m,'B')
			m+=2
		m=1
		for i in range (1,r+1):
			ans.insert(len(ans)-m,'R')
			m+=2		
		print("6Case #{}: {}".format(ij,''.join(ans)))		
	
