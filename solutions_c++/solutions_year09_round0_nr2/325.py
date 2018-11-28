#include<stdio.h>
#include<queue>
#include<memory.h>
using namespace std;
#define maxn 110
int hash[maxn][maxn];
int map[maxn][maxn];
int n, m;
int dir[4][2] = {-1, 0, 0, -1, 0, 1, 1, 0};
struct node
{
	int x, y;
}cre, now;
queue  < node > Q;
bool isok(int p, int q)
{
	int i, x, y;
	for(i= 0; i < 4; i++)
	{
		x = p + dir[i][0];
		y = q + dir[i][1];
		if (x < 0 || x >= n || y < 0 || y >= m)
			continue;
		if (map[x][y] < map[p][q])
			return false;
	}
	return true;
}
bool judge(node a, node b)
{
	int i, x, y, val; 
	node c;
	val = map[a.x][a.y];
	c.x = c.y = -1;
	for(i = 0; i < 4; i++)
	{
		x = a.x + dir[i][0];
		y = a.y + dir[i][1];
		if (x < 0 || x >= n || y < 0 || y >= m)
			continue;
		if (map[x][y] < val)
		{
			val = map[x][y];
			c.x = x;
			c.y = y;
		}
	}
	if ((c.x == b.x) && (c.y == b.y))
		return true;
	return false;
}
void bfs(int p, int q, int id)
{
	int  i , j, x, y;
	while(!Q.empty())
		Q.pop();
	now.x = p; now.y = q;
	hash[p][q] = id;
	Q.push(now);
	while(!Q.empty())
	{
		now = Q.front();
		Q.pop();
		for(i = 0; i < 4; i++)
		{
			x = now.x + dir[i][0];
			y = now.y + dir[i][1];
			if (x < 0 || x >= n || y < 0 || y >= m)
				continue;
			if (hash[x][y] != -1)
				continue;
			cre.x = x;
			cre.y = y;
			if (judge(cre, now))
			{
				hash[x][y] = id;
				Q.push(cre);
			}
		}
	}
}
int main()
{
	int hh[300];
	int cas, id, i, j, nca;
	freopen("B.in","r",stdin);
	freopen("2B.txt","w",stdout);
	scanf("%d",&cas);
	nca = 0;
	while(cas--)
	{
		nca++;
		scanf("%d%d",&n,&m);
		memset(hash, -1, sizeof(hash));
		id = 0;
		for(i = 0 ; i < n; i++)
			for(j = 0; j < m; j++)
				scanf("%d",&map[i][j]);
		for(i = 0; i < n; i++)
			for(j = 0; j < m; j++)
				if (isok(i,j))
				{
					bfs(i, j, id);
					id++;
				}
		memset(hh, -1, sizeof(hh));
		id = 0;
		for(i = 0; i < n; i++)
			for(j = 0; j < m; j++)
				if (hh[hash[i][j]] == -1)
				{
					hh[hash[i][j]] = id++;
				}
		printf("Case #%d:\n",nca);
		for(i = 0; i < n; i++)
		{
			for(j = 0; j < m - 1; j++)
			{
				printf("%c ",hh[hash[i][j]] + 'a');
			}
			printf("%c\n",hh[hash[i][j]] + 'a');
		}
	}
}