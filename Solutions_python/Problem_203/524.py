for _ in range(int(input())):
	r,c=[int(i) for i in input().split()]
	ans='Case #'+str(_+1)
	arr=[]
	val=[]
	for i in range(r):
		s=input()
		arr.append(s)
		for i in s:
			if i!='?':
				val.append(i)
	chk=0
	it=0
	while(chk==0):
		it+=1
		if it>=3:
			# print('in')
			# for i in arr:
			# 	print(i)
			# break
			if it==3:
				l=[]
				s=''
				k=0
				for j in range(c):
					s=''
					for i in arr:
						s+=i[j]
					l.append(s)
			# print(l,'#')
			for i in range(len(l)):
				chk=1
				row=l[i]
				if it%2==0:
					row=row[::-1]
				s=''
				if '?' in row:
					curr='?'
					for j in range(len(row)):
						if row[j]=='?' and curr!='?':
							s+=curr
						elif row[j]=='?' and curr=='?':
							s+='?'
							chk=0
						else:
							curr=row[j]
							s+=curr
					# print(s,'##')
					if it%2==0:
						l[i]=s[::-1]
					else:
						l[i]=s
						# print(l,'###')
			# print(l,'###')
			if chk==1:
				arr=[]
				# print(l)
				for j in range(r):
					s=''
					for i in l:
						s+=i[j]
						# print(s,'####')
					arr.append(s)
				


		else:
			for i in range(len(arr)):
				chk=1
				row=arr[i]
				if it%2==0:
					row=row[::-1]
				s=''
				if '?' in row:
					curr='?'
					for j in range(len(row)):
						if row[j]=='?' and curr!='?':
							s+=curr
						elif row[j]=='?' and curr=='?':
							s+='?'
							chk=0
							# print('###')
						else:
							curr=row[j]
							s+=curr
					if it%2==0:
						arr[i]=s[::-1]
					else:
						arr[i]=s
		for i in arr:
			if '?' in i:
				chk=0
	print(ans+':')
	for i in arr:
		# if i=='?'*c:
			# print()
		print(i)