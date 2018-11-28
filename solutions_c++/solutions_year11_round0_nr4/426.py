#include <stdio.h>
int tot,n;
int a[1010],b[1010];
int main()
{
	freopen("D-large.in","r",stdin);
	freopen("D-large.out","w",stdout);
	scanf("%d",&tot);
	for(int i=1;i<=tot;i++)
	{
		scanf("%d",&n);
		for(int j=1;j<=n;j++)
		{
			scanf("%d",&a[j]);
			b[j]=0;
		}
		double ans=0.0;
		for(int j=1;j<=n;j++)
			if(b[j]==0)
			{
				double tt=0.0;
				int kk=a[j];
				while(kk!=j)
				{
					b[kk]=1;
					kk=a[kk];
					tt=tt+1.0;
				}
				b[j]=1;
				tt=tt+1.0;
				if(tt!=1)ans+=tt;
			}
		printf("Case #%d: %.6f\n",i,ans);
	}
	return 0;
}
