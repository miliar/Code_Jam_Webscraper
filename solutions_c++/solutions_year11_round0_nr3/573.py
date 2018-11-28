#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
int t,n;

int main()
{
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	scanf("%d",&t);
	for (int tt=1;tt<=t;tt++)
	{
		scanf("%d",&n);
		int c,s=0,m,sum=0;
		for (int i=1;i<=n;i++)
		{
			scanf("%d",&c);
			s^=c;
			if (i==1 || m>c)
				m=c;
			sum+=c;
		}
		if (s)
			printf("Case #%d: NO\n",tt);
		else printf("Case #%d: %d\n",tt,sum-m);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}