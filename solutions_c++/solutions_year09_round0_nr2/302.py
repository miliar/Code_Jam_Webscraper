#include <iostream>
#include <string>
#include <vector>
#include <stack>
#include <cstdlib>
#include <ctime>
#include <queue>
using namespace std;

int n,m,g[100][100],di[4][2]={{-1,0},{0,-1},{0,1},{1,0}};
char ans[100][100],ch;

int isin(int x,int y)
{
	return x>=0 && x < n && y >=0 && y < m;
}

int find(int a , int b , int& a2, int& b2)
{
	int an = 1<<30,x,y,i;
	for (i = 0 ; i < 4 ; i++)
	{
		x = a+di[i][0]; 
		y = b+di[i][1];
		if(isin(x,y) && g[x][y] < g[a][b] && g[x][y] < an)
		{
			an = g[x][y];
			a2 = x;
			b2 = y;
		}
	}
	return an < (1<<30);
}


void dfs(int r, int c)
{
	ans[r][c] = ch;
	int i,t,x,y,x1,y1;
	for (i = 0 ; i < 4 ; i++)
	{
		x = r+di[i][0];
		y = c+di[i][1];
		if(isin(x,y) && !ans[x][y])
		{
			t = find(x,y,x1,y1);
			if(t && x1==r && y1 == c)
			{
				dfs(x,y);
			}
			t = find(r,c,x1,y1);
			if(t && x == x1 && y == y1) dfs(x1,y1);
		}
	}
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T, ca, i , j;
	scanf("%d",&T);
	for (ca = 1 ; ca <= T ; ca++)
	{
		ch = 'a';
		scanf("%d%d",&n,&m);
		for (i = 0 ; i < n ; i++)
			for (j = 0 ; j < m ; j++)
				scanf("%d",&g[i][j]);
		memset(ans,0 , sizeof ans);
		for (i = 0 ; i < n ; i++)
		{
			for (j = 0 ; j < m ; j++)
			{
				if(ans[i][j])continue;
				dfs(i,j);
				ch++;
			}
		}
		printf("Case #%d:\n",ca);
		for (i = 0 ; i < n ; i++)
		{
			for (j = 0 ; j+1 < m ; j++)
			{
				printf("%c ",ans[i][j]);
			}
			printf("%c\n",ans[i][j]);
		}
	}
	return 0;
}
