#include <stdio.h>
int main()
{
	int i,repeat,n,m,ri=1,ct;
	freopen("2.in","r",stdin);
	freopen("2.out","w",stdout);

	scanf("%d",&repeat);
	while(repeat--)
	{
		scanf("%d",&n);
		ct=0;
		for(i=1;i<=n;i++)
		{
			scanf("%d",&m);
			if( i!=m ) ct++;
		}
		printf("Case #%d: %d.000000\n",ri++,ct);
	}
	return 0;
}