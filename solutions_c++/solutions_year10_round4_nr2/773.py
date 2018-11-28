#include <cstdio>
#include <cstring>

int N,K;
int er[14];
int a[12][1024];
int buy[12][1024];
int x[2048];

void work()
{
	int T;
	int cas;
	int i,j,k,re;
	
	
	scanf("%d",&T);
	for (cas=1;cas<=T;cas++)
	{
		re=0;
		scanf("%d",&N);
		memset(buy,0,sizeof(buy));
		
		for (i=1;i<=er[N];i++)
		{
			scanf("%d",&x[i]);
		}
		
		for (i=1;i<=N;i++)
		{
			for (j=1;j<=er[N-i];j++)
			{
				scanf("%d",&a[i][j]);				
			}
		}
		/*printf("=============\n");
		for (i=1;i<=er[N];i++)
		{
			printf("%d\n",x[i]);
		}
		printf("=============\n");*/
		
		for (i=1;i<=er[N];i++)
		{
			k=0;
			for (j=N;j>x[i];j--)
			{
				if (buy[j][k+1])
				{
					;
				}
				else
				{
					buy[j][k+1]=1;
					re+=a[j][k+1];
				}
				if (er[j-1] & (i-1))
				{
					k=k*2+1;
				}
				else
				{
					k=k*2;
				}
			}			
		}
		
		/*printf("=============\n");
		for (i=1;i<=N;i++)
		{
			for (j=1;j<=N;j++)
				printf("%c",che[i][j]);
			printf("\n");
		}
		printf("=============\n");
		*/
		
		printf("Case #%d: %d\n",cas,re);
	
	}
}

int main()
{
	int i;
	
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	
	er[0]=1;
	for (i=1;i<=12;i++)
		er[i]=er[i-1]<<1;
	
	work();

	
	return 0;
}
