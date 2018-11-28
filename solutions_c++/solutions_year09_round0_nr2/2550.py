#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <malloc.h>
#include <algorithm>
using namespace std;
#define N 1001

int map[200][200];
int H, W; 

typedef struct {int x, y; }Node;
Node node[100000];
int v[200][200];
int cov[200][200];
int ans[200][200];
int dir[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};
int ps, tot;
int cmp(int a, int b)
{
	return a > b;
}
int DFS(int x, int y)
{
    int i, j;
	int xx, yy;
	int xxx, yyy;
	int t;
	int flag;
	int tmp = map[x][y];
	if(v[x][y] != -1)
	{
		ps = ans[x][y];
		return 0;
	}
	v[x][y] = 1;
	if(cov[x][y] == 0) 
	{
	    ps = ++tot;
	    cov[x][y] = ps;
	    ans[x][y] = ps;
	    return 0;
	}
	if(cov[x][y] != -1 && cov[x][y] != 0) 
	{
	    ps = cov[x][y]; 
	    return 0;
	}
	flag = 0;
	for(i = 0; i < 4; i++)
	{
		xx = x + dir[i][0];
		yy = y + dir[i][1];
		if(xx >= 0 && xx < H && yy >= 0 && yy < W && tmp > map[xx][yy])
		{
			xxx = xx;
			yyy = yy;
			flag = 1;
			tmp = map[xx][yy];
		}
	}
	if(flag == 1)
	{
 		DFS(xxx, yyy);
	 	ans[x][y] = ps;	
	}
	return 0;
}

int Solve()
{
	int i, j, k;
	int x, y;
	int tmp;
	int flag;
	memset(cov, -1, sizeof(v));
	for(i = 0; i < H; i++)
	{
		for(j = 0; j < W; j++)
		{
			tmp = map[i][j];
			flag = 1;
			for(k = 0; k < 4; k++)
			{
		    	x = i + dir[k][0];
		    	y = j + dir[k][1];
		    	if(x >= 0 && x < H && y >= 0 && y < W && tmp > map[x][y])
		    	{
		    		flag = 0;
		    		break;
		    	}
			}
			if(flag == 1) 
			{
				cov[i][j] = 0;
			}
		}
	}
	return 0;
}
					
int main()
{
    int i, j, k;
    int T; 
    int x, y;
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int cases = 1;
    scanf("%d", &T);
    while(T--)
    {
    	scanf("%d %d", &H, &W);
		for(i = 0; i < H; i++)
		    for(j = 0; j < W; j++)
		        scanf("%d", &map[i][j]);
  		memset(v, -1, sizeof(v));
  		Solve();
  		tot = 0;
  		for(i = 0; i < H; i++)
  		{
  			for(j = 0; j < W; j++)
  			{
  				if(v[i][j] != -1) continue;	
  				DFS(i, j);
  			}
  		}
  		printf("Case #%d:\n", cases++);
  		for(i = 0; i < H; i++)
  		{
  			for(j = 0; j < W; j++)
  			{
  				if(j == 0) printf("%c", 'a'+ans[i][j]-1);
  				else printf(" %c", 'a'+ans[i][j]-1);
  			}
  			printf("\n");
  		}
    }
    return 0;
}
