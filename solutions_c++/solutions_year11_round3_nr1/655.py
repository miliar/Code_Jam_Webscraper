#include <cstdio>
#include <cstring>
#include <algorithm>
#define MAX 64
using namespace std;

int R,C;
char grid[MAX][MAX];

bool solve()
{
	for(int i=0;i<R;i++)
	{
		for(int j=0;j<C;j++)
		{
			if(grid[i][j]=='#')
			{
				if(grid[i][j+1]=='#' && grid[i+1][j]=='#' && grid[i+1][j+1]=='#')
				{
					grid[i][j]='/';
					grid[i][j+1]='\\';
					grid[i+1][j]='\\';
					grid[i+1][j+1]='/';
				}
				else return false;
			}
		}
	}
	return true;
}

int main()
{
	int cases;

	scanf("%d",&cases);
	
	for(int iD=1;iD<=cases;iD++)
	{
		printf("Case #%d:\n",iD);
		
		memset(grid,0,sizeof grid);
		scanf("%d %d",&R,&C);
		for(int i=0;i<R;i++)
			scanf("%s",grid[i]);
		if(solve()) 
		{
			for(int i=0;i<R;i++)
				puts(grid[i]);
		}
		else puts("Impossible");

	}

	return 0;
}

