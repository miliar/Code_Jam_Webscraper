#include <stdio.h>
#include <stdlib.h>

const int N = 110, M = 1001111, INF = 10000,
dx[4]={-1,0,0,1},
dy[4]={0,-1,1,0};

struct pos
{
	int x,y;
}q[M];

int a[N][N],n,m;
char mark[N][N];
int to[N][N];

bool ok(int x,int y)
{
	return 0<=x && x<n && 0<=y && y<m ;
}
int main()
{

	int i,j,k,t,d;
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&t);
	for(k=1;k<=t;++k)
	{
		scanf("%d%d",&n,&m);
		for(i=0;i<n;i++)

			for(j=0;j<m;j++)
			{
				scanf("%d",&a[i][j]);
				mark[i][j]=0;
				//to[i][j] = from[i][j]= -1;
				to[i][j]=-1;
			}

		for(i=0;i<n;++i)
		{
			for(j=0;j<m;++j)
			{
				int low=a[i][j], lowdir=-1;
				for(d=0;d<4;++d)
				{
					int x=i+dx[d], y=j+dy[d];
					if(ok(x,y) && a[x][y]<low)
					{
						low = a[x][y];
						lowdir = d;
					}

				}
				if(lowdir==-1)continue;
				to[i][j] = lowdir;
				//from[i+dx[lowdir]][j+dy[lowdir]][3-lowdir] = true;
			}
		}

		char ch = 'a';
		printf("Case #%d:\n", k);

		for(i=0;i<n;++i)
		{
			for(j=0;j<m;++j)
			{
				if(mark[i][j]==0)
				{

					int fp=1, rp=1;

					q[fp].x = i;
					q[fp].y = j;


					while(fp<=rp)
					{
					    int x=q[fp].x, y=q[fp].y;
					    fp++;
					    mark[x][y]=ch;
						if(to[x][y]!=-1)
						{
							rp++;
							q[rp].x = x + dx[to[x][y]];
							q[rp].y = y + dy[to[x][y]];
							if(!ok(q[rp].x,q[rp].y) || mark[q[rp].x][q[rp].y]) rp--;

						}
						for(d=0;d<4;++d)
						{
							rp++;
							q[rp].x = x + dx[d];
							q[rp].y = y + dy[d];
							if(!ok(q[rp].x,q[rp].y) || mark[q[rp].x][q[rp].y]
							|| to[q[rp].x][q[rp].y]==-1 || to[q[rp].x][q[rp].y]+d!=3) rp--;
						}
							

					}

					ch++;
				}

			}
		}

		for(i=0;i<n;++i)
		{
			for(j=0;j<m-1;++j)
			{
				printf("%c ",mark[i][j]);
			}
			printf("%c\n",mark[i][j]);
		}
	}
	
	return 0;
}
