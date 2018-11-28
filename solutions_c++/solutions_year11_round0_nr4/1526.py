#include <stdio.h>
int main()
{
	int repeat,n,i,num,ct,ri=1;
	freopen("2.in","r",stdin);
	freopen("2.out","w",stdout);

	scanf("%d",&repeat);
	while(repeat--)
	{
		scanf("%d",&n);
		ct=0;
		for(i=1;i<=n;i++)
		{
			scanf("%d",&num);
			if( i-num ) ct++;
		}
		printf("Case #%d: %d.000000\n",ri++,ct);
	}
	return 0;
}