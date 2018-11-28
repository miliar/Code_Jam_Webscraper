#include<cstdio>
#include<algorithm>
#include<string>
#include<cstring>
#include<vector>
#include<queue>
#include<iostream>
#include<sstream>
#include<functional>
#include<map>
#include<set>

using namespace std;

typedef long long int64;
typedef pair<int,int> pint;

const int mask=10007;

int grid[102][102];
int dp[102][102];
int H, W, R;

int valid(int x,int y)
{
	return x<H && x>=0 && y<W && y>=0 && grid[x][y]==0;
}
int dfs(int x, int y)
{
	//if(x==H-1 && y==W-

	int &ret=dp[x][y];
	if(ret>=0)
		return ret;
	ret=0;
	if(valid(x+2, y+1))
		ret=(ret+dfs(x+2, y+1))%mask;
	if(valid(x+1, y+2))
		ret=(ret+dfs(x+1,y+2))%mask;

	return ret;
}
int main()
{
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("D-small-attempt0.out", "w", stdout);
	
	int numCase;
	scanf("%d", &numCase);
	for(int c=1; c<=numCase; c++)
	{
		memset(grid,0,sizeof(grid));
		memset(dp,-1,sizeof(dp));

		scanf("%d%d%d", &H,&W,&R);
		for(int i=0; i<R; i++)
		{
			int r,c;
			scanf("%d%d", &r,&c);
			grid[r-1][c-1]=1;
		}
		
		dp[H-1][W-1]=1;
		
		dfs(0,0);
		printf("Case #%d: ", c);
		printf("%d\n", dp[0][0]); 
	}
	return 0;
}