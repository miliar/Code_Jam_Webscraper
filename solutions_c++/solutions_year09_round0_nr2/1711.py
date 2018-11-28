#include<stdio.h>
#include<string.h>
const int NMAX = 128;
int map[NMAX][NMAX];
char color[NMAX][NMAX];
int dirx[4] = {-1,0 ,0,1};
int diry[4] = {0 ,-1,1,0};
int H,W;
char num ;

void init()
{
	scanf("%d%d",&H,&W);
//	printf("%d %d\n",H,W);
	int i,j;
	for( i = 0 ; i < H ;i ++ )
	{
		for( j = 0 ; j < W ; j ++ )
		{
			scanf("%d",map[i]+j);
//			printf("%d ",map[i][j]);
		}
	}
//	puts("");
	memset(color,'0',sizeof(color));
	num = 'a' ;
}
bool isIn(int i,int j )
{
	return i>=0 && i<H && j>=0 && j < W;
}
void dfs(int idx, int idy){
//	printf("%d %d\n",idx,idy);
	int i;
	int s = -1 ;
	int min = 2000000;
	for( i = 0 ; i < 4 ; i ++ )
	{
		int dx = idx + dirx[i];
		int dy = idy + diry[i];
		if( isIn(dx,dy))
		{
			if(map[idx][idy] > map[dx][dy])
			{
				if(min > map[dx][dy])
				{
					min = map[dx][dy];
					s = i;
				}
			}
		}
	}
	if( s == -1 )
		color[idx][idy] = num ++ ;
	else
	{
		int dx = idx + dirx[s];
		int dy = idy + diry[s];
		if( color[dx][dy] =='0' )
			dfs(dx,dy);
		color[idx][idy] = color[dx][dy];
	}
	
}
void run()
{
	int i,j;
	for( i = 0 ; i < H ;i ++ )
	{
		for( j = 0 ; j < W ; j ++ )
		{
			if( color[i][j] =='0')
				dfs(i,j);
		}
	}
	for( i = 0 ;i < H ; i ++ )
	{
		for( j = 0 ; j < W ; j ++ )
		{
			printf("%c ",color[i][j]);
		}
		printf("\n");
	}
}
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	scanf("%d",&T);
	int i;
	for( i = 0 ; i < T ; i++ )
	{
		printf("Case #%d:\n",i+1 );
		init();
		run();
	}
	return 0;
}