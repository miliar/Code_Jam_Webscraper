#include <cstdio>
int abs(int x)
{
	return x<0?-x:x;
}
int gcd(int a,int b)
{
	if(a<b){int c=b;b=a;a=c;}
	while(b)
	{
		int c=b;
		b=a%b;a=c;
	}
	return a;
}
int main()
{
	freopen("2.in","r",stdin);
	freopen("2.out","w",stdout);
	int c;
	scanf("%d",&c);
	for(int i=1;i<=c;++i)
	{
		int n,t,ans=0,result,tmp;
		scanf("%d",&n);
		int t0;
		if(n==1)
		{scanf("%d",&t0);ans=1;}
		else
		{
			scanf("%d",&t0);
			for(int j=1;j<n;++j)
			{
				scanf("%d",&t);
				ans=gcd(ans,abs(t-t0));
			}
		}
		tmp=t0%ans;
		if(tmp)result=ans-tmp;
		else result=0;
		printf("Case #%d: %d\n",i,result);
	}
}
