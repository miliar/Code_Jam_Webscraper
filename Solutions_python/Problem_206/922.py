import sys
f=open('input.txt','r')
f2=open('output.txt','w')
for _ in range(int(f.readline())):

	d,n=map(int,f.readline().split())
	t=0
	maxx=0
	for i in range(n):
		dist,sp=map(int,f.readline().split())
		dist=d-dist
		t=dist/sp
		maxx=max(maxx,t)
	ans=d/maxx
	f2.write("Case #%d: %.8f"%(_+1,ans))
	f2.write('\n')