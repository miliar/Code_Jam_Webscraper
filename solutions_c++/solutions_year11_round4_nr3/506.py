#include"stdio.h"
int sieve[1000001];
unsigned long long ans(unsigned long long n)
{
	if(n==1)return 0;
	unsigned long long a=1,x=2,y=x*x;
	while((y=(x*x))<=n)
	{
		if(sieve[x]==0)
			while(y<=n)
			{
				a++;
				y*=x;
			}
			x++;
	}
	return a;
}
int main()
{
	sieve[0]=sieve[1]=1;
	for(int x=2;x<1001;x++)
	{
		if(sieve[x]==0)
		for(int y=x*x;y<1000001;y+=x)sieve[y]=1;
	}
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		unsigned long long n;
		scanf("%Lu",&n); 
		printf("Case #%d: %Ld\n",t,ans(n));
	}
}
