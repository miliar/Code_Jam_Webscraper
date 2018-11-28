#include<stdio.h>
#include<string.h>
__int64 n,r,x,y;
__int64 gcd(__int64 a,__int64 b)
{
	__int64 z;
	while(b)
	{
		z=a%b;
		a=b;
		b=z;	
	}
	return a;
}
int main()
{
	int t,ca=1;
	//freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		scanf("%I64d%I64d%I64d",&n,&x,&y);
		printf("Case #%d: ",ca++);
		if(!x&&!y){puts("Possible");continue;}
		if(!y){puts("Broken");continue;}
		if(x==100&&y==100){puts("Possible");continue;}
		if(y==100){puts("Broken");continue;}
		r=100/gcd(x,100);
		if(r<=n)puts("Possible");
		else puts("Broken");
	}
}
