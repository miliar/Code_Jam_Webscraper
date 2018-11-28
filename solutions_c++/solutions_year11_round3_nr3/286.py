#include <stdio.h>

int ok(int a, int b)
{
	if (b==0) return 1;
	if (a%b==0) return 1;
	if (a==0) return 1;
	if (b%a==0) return 1;
	return 0;
}

int main()
{
	int t,n,l,h,i,k,a[108];
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	scanf("%d",&t);
	for (int cas=1; cas<=t; cas++)
	{
		scanf("%d%d%d",&n,&l,&h);
		for (i=0; i<n; i++) scanf("%d",&a[i]);
		for (i=l; i<=h; i++)
		{
			for (k=0; k<n; k++) if (ok(a[k],i)==0)
			{
				break;
			}
			if (k==n) break;
		}
		if (i<=h) printf("Case #%d: %d\n",cas,i);
		else printf("Case #%d: NO\n",cas);
	}
	return 0;
}

