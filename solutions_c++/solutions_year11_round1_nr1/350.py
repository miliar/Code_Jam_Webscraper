#include <cstdio>
using namespace std;
int gcd(int a,int b)
{
	while(b)
	{
		int t=a%b;
		a=b;
		b=t;
	}
	return a;
}
int main()
{
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		long long n;
		int pd,pg;
		scanf("%I64d%d%d",&n,&pd,&pg);
		bool ans=false;
		if(pg==0)
		{
			ans=pd==0;
		}
		else if(pg==100)
		{
			ans=pd==100;
		}
		else
		{
			int d=gcd(pd,100);
			ans=n>=(100/d);
		}
		printf("Case #%d: %s\n",i,ans?"Possible":"Broken");
	}
	return 0;
}
