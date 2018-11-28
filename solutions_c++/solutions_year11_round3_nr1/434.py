//A

#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{
	//files
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	//vars
	int T,t;
	int sy,sx,y,x;
	char grid[60][60];
	//testcase loop
	scanf("%d",&T);
		for (t=1; t<=T; t++)
		{
			//input
			scanf("%d%d\n",&sy,&sx);
				for (y=0; y<sy; y++)
					scanf("%s\n",&grid[y]);
			//greedy
			printf("Case #%d:\n",t);
				for (y=0; y<sy; y++)
					for (x=0; x<sx; x++)
						if (grid[y][x]=='#')
						{
								if ((y==sy-1) || (x==sx-1) || (grid[y+1][x]=='.') || (grid[y][x+1]=='.') || (grid[y+1][x+1]=='.'))
									goto imp;
							grid[y][x]=grid[y+1][x+1]='/';
							grid[y+1][x]=grid[y][x+1]=92;
						}
			//output
				for (y=0; y<sy; y++)
					printf("%s\n",grid[y]);
			continue;
imp:
			printf("Impossible\n");
		}
	return(0);
}