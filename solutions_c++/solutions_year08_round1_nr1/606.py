#include <stdio.h>
#include <algorithm>

using namespace std;

__int64 v1[1000],v2[1000];

int main()
{
	int t,n,i,Case=1;
	freopen("A-large.in","r",stdin);
	freopen("A-large.ou","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			scanf("%I64d",&v1[i]);
		}
		sort(v1,v1+n);
		for(i=0;i<n;i++)
		{
			scanf("%I64d",&v2[i]);
		}
		sort(v2,v2+n);
		__int64 ans=0;
		for(i=0;i<n;i++)
		{
			ans+=v1[i]*v2[n-i-1];
		}
		printf("Case #%d: %I64d\n",Case,ans);
		Case++;
	}
	return 0;
}