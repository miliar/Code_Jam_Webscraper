#include<cstdio>
int i,t,mt,ans,a,n;
int main()
{
	freopen("Dl.in","r",stdin);
	freopen("D3.out","w",stdout);
	scanf("%d",&t);
	for(mt=1;mt<=t;mt++)
	{
		ans=0;
		scanf("%d",&n);
		for(i=1;i<=n;i++)
		{
			scanf("%d",&a);
			if (a!=i) ans++;
		}
		printf("Case #%d: %.6f\n",mt,(double)ans);
	}
}
