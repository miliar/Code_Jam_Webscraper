#include<algorithm>
using namespace std;
int d[10000];
int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int i,t,tt,n,ans,pp;
	scanf("%d",&t);
	for(tt=1;tt<=t;tt++)
	{
		scanf("%d",&n);
		for(pp=ans=i=0;i<n;i++)
		{
			scanf("%d",&d[i]);
			pp^=d[i];
			ans+=d[i];
		}
		sort(d,d+n);
		ans-=d[0];
		if(pp)printf("Case #%d: NO\n",tt);
		else printf("Case #%d: %d\n",tt,ans);
	}
	return 0;
}
