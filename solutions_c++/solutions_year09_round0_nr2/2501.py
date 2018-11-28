#include<iostream>
#include<queue>
using namespace std;

int H, W;
int map[101][101];
int dir[][2] = {-1,0, 0,-1, 0,1, 1,0};
char str[101][101];
char ch;


struct Q
{
	int x, y;
};
Q p, tp;
queue <Q> q;
int hash[4] = {3, 2, 1, 0};
void bfs(int a, int b)
{
	int i, k, si, sj, minist, v;
	while(!q.empty())
	{
		p = q.front();
		q.pop();
		minist = map[p.x][p.y];
		v = -1;
		for(i = 0; i < 4; i ++)
		{
			si = p.x + dir[i][0];
			sj = p.y + dir[i][1];
			if(si >= 0 && si < H && sj >= 0 && sj < W)
			{
				if(minist > map[si][sj])
				{
					minist = map[si][sj];
					v = i;
				}
				if(map[p.x][p.y] < map[si][sj] && str[si][sj] == 0)
				{
					for(k = 0; k < 4; k ++)
					{
						tp.x = si + dir[k][0];
						tp.y = sj + dir[k][1];
						if(tp.x >= 0 && tp.x < H && tp.y >= 0 && tp.y < W && (map[tp.x][tp.y] < map[p.x][p.y] || (map[tp.x][tp.y] == map[p.x][p.y] && k < hash[i])))
							break;
					}
					if(k == 4)
					{ 
						str[si][sj] = ch;
						tp.x = si;
						tp.y = sj;
						q.push(tp);
					}
				}
			}
		}
		if(v != -1 && str[p.x + dir[v][0]][p.y + dir[v][1]] == 0)
		{
			str[p.x + dir[v][0]][p.y + dir[v][1]] = ch;
			tp.x = p.x + dir[v][0];
			tp.y = p.y + dir[v][1];
			q.push(tp);
		} 
	}
	return ;
}
int main()
{
	freopen("B-small-attempt2.in", "r", stdin);
	freopen("feifan.txt", "w",stdout);
	int i, j, e, T;  
	scanf("%d", &T);
	for(e = 1; e <= T; e ++)
	{
		scanf("%d %d", &H, &W);
		ch = 'a';
		for(i = 0; i < H; i ++)
			for(j = 0; j < W; j ++)
			{
				str[i][j] = 0;
				scanf("%d", &map[i][j]);
			}
		for(i = 0; i < H; i ++)
			for(j = 0; j < W; j ++)
			{
				if(str[i][j] == 0)
				{
					while(!q.empty())
						q.pop();
					p.x = i;
					p.y = j;
					q.push(p);
					str[i][j] = ch;
					bfs(i, j);
					ch ++;
				}
			}
		printf("Case #%d:\n", e);
		for(i = 0; i < H; i ++)
		{
			for(j = 0; j < W; j ++)
			{
				if(j > 0) printf(" ");
				printf("%c", str[i][j]);
			}
			printf("\n");
		}
	}
	return 0;
}
