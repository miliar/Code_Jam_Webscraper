#include <stdio.h>
#include <stdlib.h>
#include <memory.h>
#include <vector>
#include <algorithm>
using namespace std;

int T,H,W,h[100][100],v[4][2] = {{-1,0},{0,-1},{0,1},{1,0}},map[100][100],to[100][100][2],cnt;

bool valid(int x,int y)
{
	return x >= 0 && x < H && y >= 0 && y < W;
}

void dfs(int x,int y)
{
	if(to[x][y][0] == -1)
		map[x][y] = cnt,cnt++;
	else if(map[to[x][y][0]][to[x][y][1]] != -1)
		map[x][y] = map[to[x][y][0]][to[x][y][1]];
	else
	{
		dfs(to[x][y][0],to[x][y][1]);
		map[x][y] = map[to[x][y][0]][to[x][y][1]];
	}
}
		
int main()
{
	int i,j,k,t,cx,cy,x,y;
	//freopen("2_s.txt","w",stdout);
	//freopen("B-small-attempt1.in","r",stdin);
	scanf("%d",&T);
	for(t = 1;t <= T;t++)
	{
		scanf("%d%d",&H,&W);
		for(i = 0;i < H;i++)
			for(j = 0;j < W;j++)
				scanf("%d",&h[i][j]);
		memset(to,-1,sizeof(to));
		for(i = 0;i < H;i++)
			for(j = 0;j < W;j++)
			{
				cx = cy = -1;
				for(k = 0;k < 4;k++)
				{
					x = i + v[k][0],y = j + v[k][1];
					if(valid(x,y) && h[x][y] < h[i][j])
					{
						if(cx == -1 || h[x][y] < h[cx][cy])
							cx = x,cy = y;
					}
				}
				if(cx != -1)
					to[i][j][0] = cx,to[i][j][1] = cy;
			}
		memset(map,-1,sizeof(map));
		cnt = 0;
		for(i = 0;i < H;i++)
			for(j = 0;j < W;j++)
			{
				if(map[i][j] == -1)
					dfs(i,j);
			}
		printf("Case #%d:\n",t);
		for(i = 0;i < H;i++)
		{
			for(j = 0;j < W;j++)
				printf("%c ",map[i][j] + 'a');
			printf("\n");
		}
	}
	//system("PAUSE");
	return 0;
}
				
		
