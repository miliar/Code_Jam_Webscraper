#include <cstdio>
#include <cstring>

int N,K;
char che[64][64];
int dy[4]={0,1,1,-1};
int dx[4]={1,0,1,1};
int kdy[4]={0,1,1,-1},kdx[4]={1,0,1,1};

int check(int y,int x)
{
	int i,j,ok;
	int hy,hx;
	
	
	for (i=0;i<4;i++)
	{
		if (kdy[i]*(K-1)+y>=1 && kdy[i]*(K-1)+y<=N && kdx[i]*(K-1)+x>=1 && kdx[i]*(K-1)+x<=N)
		{
			hy=y;
			hx=x;
			ok=1;
			for (j=1;j<K;j++)
			{
				hy+=dy[i];
				hx+=dx[i];
				if (che[y][x]!=che[hy][hx])
				{
					ok=0;
					break;
				}
			}
			if (ok)
				return 1;
		}
	}
	return 0;
}


void work()
{
	int T;
	int cas;
	int i,j,k,rflag,bflag;
	char rtmp[4];
	
	scanf("%d",&T);
	for (cas=1;cas<=T;cas++)
	{
		scanf("%d%d",&N,&K);
		
		
		for (i=1;i<=N;i++)
		{
			for (j=1;j<=N;j++)
			{
				scanf("%1s",&rtmp[0]);
				che[j][N-i+1]=rtmp[0];
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
		for (i=1;i<=N;i++)
		{
			for (j=N;j>=1;j--)
			{
				k=j;
				while (che[k][i]=='.' && k>=1)
					k--;
				if (k>=1 && k<j)
				{
					che[j][i]=che[k][i];
					che[k][i]='.';
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
		
		rflag=bflag=0;
		for (i=1;i<=N;i++)
		{
			for (j=1;j<=N;j++)
			{
				if (che[i][j]!='.')
					if (check(i,j))
					{
						if (che[i][j]=='R')
							rflag=1;
						else
							bflag=1;
					}
			}
		}
		
		//printf("K=%d\n",K);
		
		printf("Case #%d: ",cas);
		if (rflag && bflag)
			printf("Both\n");
		else if (rflag)
			printf("Red\n");
		else if (bflag)
			printf("Blue\n");
		else
			printf("Neither\n");
	
	}
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	work();

	
	return 0;
}
