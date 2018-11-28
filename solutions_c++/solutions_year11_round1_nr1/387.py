#include<cstdio>
#include<algorithm>
//                Last Change:  2011-05-21 09:29:12
using namespace std;
int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int _;scanf("%d",&_);
	for(int cas=1;cas<=_;++cas)
	{
		long long n,d,g;
		scanf("%I64d%I64d%I64d",&n,&d,&g);
		printf("Case #%d: ",cas);
		if(g==100&&d<100)
			puts("Broken");
		else if(d&&!g)
			puts("Broken");
		else if(!d)
			puts("Possible");
		else
		{
			long long f=__gcd(100LL,d);
			long long mx=100/f;
			if(mx>n)puts("Broken");
			else puts("Possible");
		}
	}
	return 0;
}
