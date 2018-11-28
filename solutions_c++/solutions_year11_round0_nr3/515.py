#include <iostream>
using namespace std;
int main()
{
	freopen("C-large.in","r",stdin);
	freopen("outc.text","w",stdout);
	int i,j,k,n,t,minn,ans,co=1,s;
	scanf("%d",&t);
	while (t--)
	{
		scanf("%d",&n);
		ans=0;
		s=0;
		minn=2000000000;
		for (i=0;i<n;i++)
		{
			scanf("%d",&k);
			minn=minn<k?minn:k;
			ans^=k;
			s+=k;
		}
		if (ans==0)
			printf("Case #%d: %d\n",co++,s-minn);
		else
			printf("Case #%d: NO\n",co++);
	}
	return 0;
}