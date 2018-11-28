#include<stdio.h>

int main(void)
{
	int t;
	int yy=0;
	freopen("B-large (1).in","r",stdin);
	freopen("output.out","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		unsigned long long c,l,p;
		yy++;
		scanf("%llu%llu%llu",&l,&p,&c);
		int ans=0;
		while(l*c<p)
		{
			ans++;
			c=c*c;
		}
		printf("Case #%d: %d\n",yy,ans);
	}
	return 0;
}