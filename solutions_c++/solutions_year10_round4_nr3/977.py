#include <map>
#include <cmath>
#include <vector>
#include <cstdio>
#include <string>
#include <cstring>
#include <iostream>
#include <algorithm>
#define CASES for(scanf("%d",&cases);cases--;)
#define CASEID printf("Case #%d: ",iD++);
#define MAX 105
using namespace std;

bool grid[MAX][MAX];
bool isempty()
{
	for(int i=0;i<MAX;i++)
		for(int j=0;j<MAX;j++)
			if(grid[i][j]) return false;
	return true;
}
			
int main()
{
	int R,x1,y1,x2,y2,iD=1,cases;

	CASES
	{
		cin>>R;
		memset(grid,0,sizeof grid);
		for(int i=0;i<R;i++)
		{
			cin>>x1>>y1>>x2>>y2;
			for(int i=x1;i<=x2;i++)
				for(int j=y1;j<=y2;j++)
					grid[i][j]=1;
		}
		int time=0;
		bool tmp[MAX][MAX];memcpy(tmp,grid,sizeof grid);

		while(!isempty())
		{
			for(int i=1;i<MAX;i++)
			{
				for(int j=1;j<MAX;j++)
				{
					if(grid[i-1][j]==0 && grid[i][j-1]==0)
						tmp[i][j]=0;
					else if(grid[i-1][j]==1 && grid[i][j-1]==1)
						tmp[i][j]=1;
				}
			}
			time++;
//			puts("FUCKED");
			memcpy(grid,tmp,sizeof tmp);
		}
		CASEID;
		printf("%d\n",time);			
	}
	return 0;
}
