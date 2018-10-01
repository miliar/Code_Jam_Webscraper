def gcd(a,b):
	if(b==0):
		return a;
	else:
		return gcd(b,a%b);
nt = input();
i=1;
while(i<=nt):
	s = raw_input();
	s=s.split(' ');
	n = int(s[0]);
	j=0;
	arr=[]
	while(j<n):
		p = int(s[j+1]);
		arr.append(p);
		j+=1;
	j=0;
	t=0;
	arr.sort();
	while(j<n):
		k=j+1;
                while(k<n):
			t=gcd(t,arr[k]-arr[j]);
			k+=1;
		j+=1;
	x=arr[0]%t;
	if(x):
		x = t-x;		
	print "Case #"+str(i)+": "+str(x);
	i+=1;
