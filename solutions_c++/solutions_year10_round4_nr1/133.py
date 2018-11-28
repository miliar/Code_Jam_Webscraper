#include<stdio.h>
#include<math.h>

int a[101][101];

int main()
{
	int t,p;
	int n;
	int i,j;
	int ii,jj;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&t);
	for (p=1;p<=t;p++)
	{
		scanf("%d",&n);
		for (i=1;i<=n;i++)
		{
			for (j=1;j<=n-i;j++)
				a[i][j]=-1;
			for (j=1;j<=i;j++)
			{
				scanf("%d",&a[i][n-i+2*j-1]);
				a[i][n-i+2*j]=-1;
			}
			for (j=n+i;j<2*n;j++)
				a[i][j]=-1;
		}
		for (i=n+1;i<2*n;i++)
		{
			for (j=1;j<=i-n;j++)
				a[i][j]=-1;
			for (j=1;j<=2*n-i;j++)
			{
				scanf("%d",&a[i][i-n+2*j-1]);
				a[i][i-n+2*j]=-1;
			}
			for (j=3*n-i;j<2*n;j++)
				a[i][j]=-1;
		}
		int mm=6*n-5;
		for (ii=1;ii<2*n;ii++)
			for (jj=1;jj<2*n;jj++)
			{
				int res;
				if (jj>=n) res=(jj-1+abs(ii-n))*2+1;
				else res=(2*n-1-jj+abs(ii-n))*2+1;
				if (ii>=n)
				{
					if (res<(ii-1+abs(jj-n))*2+1) res=(ii-1+abs(jj-n))*2+1;
				}
				else
				{
					if (res<(2*n-1-ii+abs(jj-n))*2+1) res=(2*n-1-ii+abs(jj-n))*2+1;
				}
				if (res>mm) continue;
				if (ii<=n)
				{
					for (i=1;i<ii;i++)
					{
						for (j=1;j<2*n;j++)
						{
							if (a[i][j]==-1) continue;
							if (a[2*ii-i][j]==-1) continue;
							if (a[i][j]!=a[2*ii-i][j]) break;
						}
						if (j<2*n) break;
					}
					if (i<ii) continue;
				}
				else
				{
					for (i=ii+1;i<2*n;i++)
					{
						for (j=1;j<2*n;j++)
						{
							if (a[i][j]==-1) continue;
							if (a[2*ii-i][j]==-1) continue;
							if (a[i][j]!=a[2*ii-i][j]) break;
						}
						if (j<2*n) break;
					}
					if (i<2*n) continue;
				}
				if (jj<=n)
				{
					for (j=1;j<jj;j++)
					{
						for (i=1;i<2*n;i++)
						{
							if (a[i][j]==-1) continue;
							if (a[i][2*jj-j]==-1) continue;
							if (a[i][j]!=a[i][2*jj-j]) break;
						}
						if (i<2*n) break;
					}
					if (j<jj) continue;
				}
				else
				{
					for (j=jj+1;j<2*n;j++)
					{
						for (i=1;i<2*n;i++)
						{
							if (a[i][j]==-1) continue;
							if (a[i][2*jj-j]==-1) continue;
							if (a[i][j]!=a[i][2*jj-j]) break;
						}
						if (i<2*n) break;
					}
					if (j<2*n) continue;
				}
				mm=res;
			}
		printf("Case #%d: %d\n",p,(mm+1)*(mm+1)/4-n*n);
	}
	return 0;
}