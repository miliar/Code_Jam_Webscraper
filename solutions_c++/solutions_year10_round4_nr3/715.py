#include <cstdio>
#include <cstring>

int N,K;
int cell[256][256],tmp[256][256];

void work()
{
	int T;
	int cas;
	int i,j,k,re,left;
	int xa,xb,ya,yb;
	
	scanf("%d",&T);
	for (cas=1;cas<=T;cas++)
	{
		re=0;
		scanf("%d",&N);
		memset(cell,0,sizeof(cell));
		
		left=0;
		for (i=1;i<=N;i++)
		{
			scanf("%d%d%d%d",&xa,&ya,&xb,&yb);				
			for (j=xa;j<=xb;j++)
			{
				for (k=ya;k<=yb;k++)
				{
					if (cell[j][k]==0)
						left++;
					cell[j][k]=1;
				}
			}
		}
		/*printf("=============\n");
		for (i=1;i<=er[N];i++)
		{
			printf("%d\n",x[i]);
		}
		printf("=============\n");*/
		
		while (left)
		{
		/*			printf("=============\n");
		for (i=1;i<=6;i++)
		{
			for (j=1;j<=6;j++)
				printf("%d",cell[j][i]);
			printf("\n");
		}
		printf("=============\n");
			*/
			re++;
			left=0;
			memset(tmp,0,sizeof(tmp));
			for (i=1;i<=100;i++)
			{			
				for (j=1;j<=100;j++)
				{
					if ((cell[i-1][j]) && (cell[i][j-1]) && (cell[i][j]==0))
					{
						left++;
						tmp[i][j]=1;
					}
					if (((cell[i-1][j]) || (cell[i][j-1])) && (cell[i][j]==1))
					{
						left++;
						tmp[i][j]=1;
					}
				}
			}
			memcpy(cell,tmp,sizeof(tmp));
		}	
		
		

		
		
		printf("Case #%d: %d\n",cas,re);
	
	}
}

int main()
{
	//int i;
	
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	
	
	work();

	
	return 0;
}
