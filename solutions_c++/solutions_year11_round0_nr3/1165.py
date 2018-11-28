#include<cstdio>
#include<algorithm>
//  Last Change:  2011-05-07 08:59:03
using namespace std;
int n,a[1003];
int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	int _;scanf("%d",&_);
	for(int cas=1;cas<=_;++cas)
	{
		scanf("%d",&n);
		for(int i=1;i<=n;++i)scanf("%d",a+i);
		int s=0;
		for(int i=1;i<=n;++i)s^=a[i];
		printf("Case #%d: ",cas);
		if(!s)
		{
			sort(a+1,a+n+1);
			int ans=0;
			for(int i=2;i<=n;++i)
				ans+=a[i];
			printf("%d\n",ans);
		}
		else puts("NO");
	}
	return 0;
}
