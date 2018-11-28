#include <cstdio>

int k,n,j,a[1500],b[1500],ans,t,tt;
int main()
{
	freopen("file.in","r",stdin);
	freopen("file.out","w",stdout);
	scanf("%d",&t);
	for(tt=0;tt<t;tt++)
	{
		scanf("%d",&n);
		for(k=0;k<n;k++)
			scanf("%d%d",&a[k],&b[k]);
		ans=0;
		for(k=0;k<n;k++)
		{
			for(j=0;j<n;j++)
			if (k!=j&&a[k]<a[j]&&b[k]>b[j]) ans++;
		}
		printf("Case #%d: %d\n",tt+1,ans);
	}
}