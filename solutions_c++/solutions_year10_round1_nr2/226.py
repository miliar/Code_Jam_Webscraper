#include <cstdio>
#include <cstring>

int D,I,M;
int a[256];
int best[128][356];
int flag[128][356];

int inline myabs(int x)
{
	return x>0?x:-x;
}

void inline update(int x, int y, int v)
{
	if (flag[x][y])
	{
		if (best[x][y]>v)
			best[x][y]=v;
	}
	else
	{
		best[x][y]=v;
		flag[x][y]=1;
	}
}

void work()
{
	int T,N;
	int cas;
	int i,j,k,re;
	
	scanf("%d",&T);
	for (cas=1;cas<=T;cas++)
	{
		scanf("%d%d%d%d",&D,&I,&M,&N);
		
		
		for (i=1;i<=N;i++)
		{
			scanf("%d",&a[i]);
		}
		memset(best,0,sizeof(best));
		memset(flag,0,sizeof(flag));
		
		for (i=0;i<=256;i++)
		{
			flag[0][i]=1;
		}
		for (i=1;i<=N;i++)
		{
			for (j=0;j<=256;j++)
			{
				for (k=0;k<=256;k++)
				{
					if (flag[i-1][k])
					{
						if (myabs(k-j)<=M)
							update(i,j,best[i-1][k]+myabs(a[i]-j));
						else
						{
							if (M>0)
							{
								update(i,j,best[i-1][k]+myabs(a[i]-j)+(myabs(k-j)-1)/M*I);
							}
							else
							{
								;
							}
						}
					}
				}
				if (flag[i-1][j])
					update(i,j,best[i-1][j]+D);
			}
		}
		
		re=99999999;
		for (i=0;i<=256;i++)
		{
			if (best[N][i]<re)
				re=best[N][i];
		}
		printf("Case #%d: %d\n",cas,re);
		
		/*for (i=1;i<=N;i++)
		{
			for (j=0;j<=10;j++)
				printf("%4d",best[i][j]);
			printf("\n");
		}*/
	}
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	work();

	
	return 0;
}
