#include <stdio.h>
#include <string.h>
#include <vector>

using namespace std;

#define MAXN 200
#define INF 999999999

int height[MAXN][MAXN];
char map[MAXN][MAXN];
int cover[MAXN][MAXN];
int H,W;

int dr[] = {-1,0,0,1};
int dc[] = {0,-1,1,0};

void dfs(int i,int j,int ch)
{
	vector < pair <int,int> > candidate;
	pair <int,int> u;

	int I,nr,nc,J;

	cover[i][j] = ch;

	for( I = 0; I < 4; I++ )
	{
		nr = i + dr[I];
		nc = j + dc[I];

		if( nr < 0 || nr >= H || nc < 0 || nc >= W || height[nr][nc] <= height[i][j] || cover[nr][nc] != -1 ) continue;
		
		candidate.push_back(make_pair(nr,nc));
	}

	for( I = 0; I < candidate.size(); I++ )
	{
		int minHeight = INF;
		for( J = 0; J < 4; J++ )
		{
			nr = candidate[I].first + dr[J];
			nc = candidate[I].second + dc[J];

			if( nr < 0 || nr >= H || nc < 0 || nc >= W || height[nr][nc] >= height[candidate[I].first][candidate[I].second] ) continue;

			if( minHeight > height[nr][nc] ) 
			{
				minHeight = height[nr][nc];
				u = make_pair(nr,nc);
			}
		}

		if( u.first == i && u.second == j ) dfs(candidate[I].first,candidate[I].second,ch);
	}
}

void solve()
{

	int i,j,minNum,minI,minJ;
	bool finished = false;
	int ch = 0;
	
	for( i = 0; i < H; i++ )
	{
		for( j = 0; j < W; j++ ) 
		{
			map[i][j] = '.';
			cover[i][j] = -1;
		}
	}

	while(!finished)
	{
		minNum = INF;
		minI = minJ = -1;

		for( i = 0; i < H; i++ )
		{
			for( j = 0; j < W; j++ )
			{
				if( minNum > height[i][j] && cover[i][j] == -1 )
				{
					minNum = height[i][j];
					minI = i,minJ = j;
				}
			}
		}

		if( minI == -1 && minJ == -1 ) finished = true;
		else dfs(minI,minJ,ch);
		ch++;
	}

	char c = 'a';

	finished = false;

	while(!finished)
	{
		for( i = 0; i < H; i++ )
		{
			for( j = 0; j < W; j++ )
			{
				if( map[i][j] == '.' )
					break;
			}
			if( j < W ) break;
		}

		if( i >= H ) finished = true;
		else
		{
			
			pair <int,int> u = make_pair(i,j);

			for( i = 0; i < H; i++ )
			{
				for( j = 0; j < W; j++ )
				{
					if( cover[i][j] == cover[u.first][u.second] )
					{
						map[i][j] = c;
					}
				}
			}
			c++;
		}
	}
}




int main()
{
	int T;
	int i,j;

	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);

	scanf("%d",&T);

	for( int kase = 1; kase <= T; kase++ )
	{
		scanf("%d %d",&H,&W);

		for(i = 0; i < H; i++)
		{
			for( j = 0; j < W; j++ )
				scanf("%d",&height[i][j]);
		}

		printf("Case #%d:\n",kase);

		solve();

		for( i = 0; i < H; i++ )
		{
			for( j = 0; j < W; j++ )
			{
				if( j != 0 ) printf(" %c",map[i][j]);
				else printf("%c",map[i][j]);
			}
			printf("\n");
		}
	}
	return 0;
}
