#include<stdio.h>

int f[11][1100][11];
int a[1100];
int inf=200000000;

int main()
{
	int t,p;
	int n;
	int i,j,k;
	int s;
	int price;
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&t);
	for (p=1;p<=t;p++)
	{
		scanf("%d",&n);
		s=1<<n;
		for (i=1;i<=s;i++)
			scanf("%d",&a[i]);
		for (i=1;i<=s;i++)
		{
			for (j=0;j<=a[i];j++)
				f[0][i][j]=0;
			for (j=a[i]+1;j<=n;j++)
				f[0][i][j]=inf;
		}
		s=s/2;
		for (k=1;k<=n;k++)
		{
			for (i=1;i<=s;i++)
			{
				scanf("%d",&price);
				f[k][i][n-k+1]=inf;
				for (j=n-k;j>=0;j--)
				{
					f[k][i][j]=price+f[k-1][2*i-1][j]+f[k-1][2*i][j];
					if (f[k][i][j]>f[k-1][2*i-1][j+1]+f[k-1][2*i][j+1]) f[k][i][j]=f[k-1][2*i-1][j+1]+f[k-1][2*i][j+1];
					if (f[k][i][j]>f[k][i][j+1]) f[k][i][j]=f[k][i][j+1];
				}
			}
			s=s/2;
		}
		printf("Case #%d: %d\n",p,f[n][1][0]);
	}
	return 0;
}

