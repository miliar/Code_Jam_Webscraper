#include <stdio.h>
#include <algorithm>
using namespace std;
int main()
{
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int cas=1;cas<=T;cas++)
	{
		int n;
		scanf("%d",&n);
		int tmp=0,sum=0,ans=100000000;
		for(int i=0;i<n;i++)
		{
			int c;
			scanf("%d",&c);
			ans=min(ans,c);
			sum+=c;
			tmp^=c;
		}
		if(tmp==0)
		printf("Case #%d: %d\n",cas,sum-ans);
		else printf("Case #%d: NO\n",cas);
	}
}
