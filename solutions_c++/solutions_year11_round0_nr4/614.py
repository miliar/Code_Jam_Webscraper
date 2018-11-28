#include <stdio.h>
int main ()
{
	int cas,ca,n,i,x,ans;
	freopen("D-large.in","r",stdin);
	freopen("D-large.out","w",stdout);
	scanf("%d",&cas);
	for(ca=1;ca<=cas;ca++)
	{
		ans=0;
		scanf("%d",&n);
		for(i=1;i<=n;i++)
		{
			scanf("%d",&x);
			if(x!=i)
				ans++;
		}
		printf("Case #%d: %d.000000\n",ca,ans);

	}
}