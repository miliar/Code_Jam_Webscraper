#include<iostream>
using namespace std;
#define MAXN 20
int main()
{
//	freopen("C-large.in","r",stdin);
//	freopen("C.out","w",stdout);

	int ct,i,tt=0;
	int n,ans,minn,sum,temp;
	scanf("%d",&ct);
	while(ct--)
	{
		scanf("%d",&n);
		scanf("%d",&ans);
		minn=ans;
		sum=ans;
		for(i=1;i<n;i++)
		{
			scanf("%d",&temp);
			sum+=temp;
			if(minn>temp)minn=temp;
			ans^=temp;
		}
		if(ans==0)
			printf("Case #%d: %d\n",++tt,sum-minn);
		else printf("Case #%d: NO\n",++tt);
	}
}