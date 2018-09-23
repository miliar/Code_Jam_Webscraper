for t in xrange(1,input()+1):
	r,c=map(int,raw_input().split())
	row=[]
	done=[False]*26
	left=26
	ans=[['' for _ in xrange(c)] for i in xrange(r)]
	for i in xrange(r):
		row.append(raw_input())
		for j in xrange(c):
			ans[i][j]=row[i][j]
			if row[i][j]!='?':
				done[ord(row[i][j])-65]=True
				left-=1

	for i in xrange(r):
		for j in xrange(c):
			if ans[i][j]!='?':
				k=j-1
				while k >=0:
					if ans[i][k]=='?':
						ans[i][k]=ans[i][j]
					else:
						break
					k-=1
				k=j+1
				while(k<c):
					if ans[i][k]=='?':
						ans[i][k]=ans[i][j]
					else:
						break
					k+=1
		#print ans,'ddd'
	#pprint ans
	for i in xrange(r):
		if ans[i][0]=='?':
			found=False
			#first search backwards
			k=i-1
			#print'in'
			while k>=0:
				if ans[k][0]!='?':
					break
				k-=1
			if k!=-1:
				for j in xrange(k+1,i+1):
					for l in xrange(c):
						ans[j][l]=ans[k][l]
			else:
				k=i+1
				#print 'last in'
				while k<r:
					if ans[k][0]!='?':
						break
					k+=1
				for j in xrange(k-1,i-1,-1):
					for l in xrange(c):
						ans[j][l]=ans[k][l]
	print 'Case',('#'+str(t)+':')
	for rw in xrange(r):
		print ''.join(ans[rw])			




		


