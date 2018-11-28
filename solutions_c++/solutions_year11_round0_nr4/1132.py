#include <cstdio>

int I,T,ans,n,m;
int main()
{
	scanf("%d",&T);
	for (I=1;I<=T;++I)
	{
		ans=0;
		scanf("%d",&n);
		for (int i=1;i<=n;++i)
		{
			scanf("%d",&m);
			if (m!=i) ++ans;
		}
		printf("Case #%d: %.7f\n",I,ans+.0);
	}
	return 0;
}
