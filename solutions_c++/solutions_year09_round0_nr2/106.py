#include <iostream>
using namespace std;
#define tiao system("pause")

char ans[111][111];
char color(0);
int t;
int row, col;

int dx[] = {-1,0,0,1};
int dy[] = {0,-1,1,0};

int aX[11111],aY[11111],lenA;
int g[111][111];

void dfs(int i, int j)
{
//	cout << i << ' ' << j; tiao;
	int low(g[i][j]), bestK(-1);
	int x,y;
	
	for (int k=0; k<4; k++)
	{
		x = i + dx[k];
		y = j + dy[k];
		
		if (g[x][y] < low)
		{
			low = g[x][y];
			bestK = k;
		}		
	}
	
	if (bestK != -1)
	{
		lenA++;
		aX[lenA] = i + dx[bestK];
		aY[lenA] = j + dy[bestK];
		dfs(i + dx[bestK], j + dy[bestK]);
	}
}

int main(void)
{
	int i,j,k,ci,cici,cicici,x,y;
	
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	
	scanf("%d",&t);
	for (int cb=1; cb<=t; cb++)
	{
		scanf("%d%d",&row,&col);
		for (i=0; i<=row+1; i++)
			g[i][0] = g[i][col+1] = 1 << 29; 
		for (i=0; i<=col+1; i++)
			g[0][i] = g[row+1][i] = 1 << 29;
			
		for (i=1; i<=row; i++)
			for (j=1; j<=col; j++)
				scanf("%d",&g[i][j]);
		
		memset(ans,0,sizeof(ans));
		color = 'a';
		for (i=1; i<=row; i++)
			for (j=1; j<=col; j++)
				if (ans[i][j] == '\0')
				{
					lenA = 1;
					aX[1] = i;
					aY[1] = j;
					
					dfs(i,j);
					if (ans[aX[lenA]][aY[lenA]] != '\0')
					{
						for (k=1; k<=lenA; k++)
							ans[aX[k]][aY[k]] = ans[aX[lenA]][aY[lenA]];
					} 
					else
					{
						for (k=1; k<=lenA; k++)
							ans[aX[k]][aY[k]] = color;
						color++;
					}
				}
		
		printf("Case #%d:\n",cb);
		for (i=1; i<=row; i++)
		{
			for (j=1; j<col; j++)
				printf("%c ",ans[i][j]);
			printf("%c\n",ans[i][j]);
		}
	}
//	tiao;
	return 0;
}

