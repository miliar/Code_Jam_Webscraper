#include <iostream>
using namespace std;
int n;
int a[1005],b[1005];
int main()
{
	int i,j,k,t,co=1,ans,m;
	freopen("D-large.in","r",stdin);
	freopen("outd.text","w",stdout);
	scanf("%d",&t);
	while (t--)
	{
		scanf("%d",&n);
		ans=0;
		memset(b,0,sizeof(b));
		for (i=1;i<=n;i++)
			scanf("%d",&a[i]);
		for (i=1;i<=n;i++)
			if (b[i]==0)
			{
				k=0;
				m=i;
				while (b[m]==0)
				{
					b[m]=1;
					k++;
					m=a[m];
				}
				if (k==1)
					k=0;
				ans+=k;
			}
		printf("Case #%d: %d\n",co++,ans);
	}
	return 0;
}