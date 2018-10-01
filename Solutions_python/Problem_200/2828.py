# your code goes here

t=int(input())
for c in range(t):
	s=input()
	l=list(s)
	l=list(map(int,l))
	# print(l)
	n=len(s)
	tem=0
	for i in range(n-2,-1,-1):
		# print(i)
		if(l[i+1]<l[i]):
			if i>0:
				tem=int(str(s[:i]))*(10**(n-i)) + (int(l[i])*(10**(n-1-i))-1)
			else :
				tem= (int(l[i])*(10**(n-1-i))-1)
			# print(tem)
			s=str(tem)
			l=list(str(tem))
	print(s);