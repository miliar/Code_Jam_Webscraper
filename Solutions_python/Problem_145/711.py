tn=int(input())
for tt in range(tn):
	print("Case #%d: "%(tt+1),end='')
	a,b = (int(i) for i in input().split('/'))
	if b%a==0:
		b/=a
		a=1
	ans=1
	test=1
	chk=True
	while test<b:
		test<<=1
	if test==b:
		while a*2<b:
			ans+=1
			a*=2
	else:ans="impossible"
	print(ans)