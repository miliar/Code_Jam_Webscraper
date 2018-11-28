#include <stdio.h>
long long gcd(long long a,long long b)
{
	long long tmp;
	while(a!=0)
	{
		tmp=a;
		a=b%a;
		b=tmp;
	}
	return b;
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("a_large.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int cas=1;cas<=T;cas++)
	{
		long long n,p,q;
		bool ans=true;
		scanf("%lld%lld%lld",&n,&p,&q);
		if((q==0&&p!=0)||(q==100&&p!=100))
		{
			ans=false;
		}
		else
		{
			long long lin=100;
			lin/=gcd(p,100);
			if(lin<=n)ans=true;
			else ans=false;
		}
		printf("Case #%d: ",cas);
		if(ans)printf("Possible\n");
		else printf("Broken\n");
	}
}
