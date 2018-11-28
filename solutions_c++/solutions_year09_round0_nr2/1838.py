#include <iostream>
#include <vector>
#include <deque>

using namespace std;

int mat[105][105];
char out[105][105];
bool visit[105][105];

struct pp
{
	int x, y;
}now, next;

vector<pp>vc;
deque<pp>dq;

int r, c;
int dir[4][2] = {{-1, 0},{0,-1},{0,1},{1,0}};
char nowkind;
void bfs()
{
	int i,j;
	char kind = 0;
	dq.clear();
	dq.push_back(now);
	visit[now.x][now.y] = 1;
	vc.clear();
	vc.push_back(now);
	while(! dq.empty())
	{
		now = dq.front();
		dq.pop_front();
		pp temp;
		temp.x = -1;
		for(i = 0; i < 4; i ++)
		{
			next.x = now.x + dir[i][0];
			next.y = now.y + dir[i][1];

			if(next.x < 0 || next.x >= r || next.y < 0 || next.y >= c)
				continue;
			if(temp.x == -1 || mat[temp.x][temp.y] > mat[next.x][next.y])
			{
				temp.x = next.x;
				temp.y = next.y;
				//if(mat[next.x][next.y] < mat[now.x][now.y])
				//{
				//	if(kind == 0 && out[next.x][next.y] != 0)
				//		kind = out[next.x][next.y];
				//	if(visit[next.x][next.y] != 0)
				//		continue;
				//	visit[next.x][next.y] = 1;
				//	vc.push_back(next);
				//}
			}
		}

		if(temp.x != -1 && mat[temp.x][temp.y] < mat[now.x][now.y])
		{
			if(kind == 0 && out[temp.x][temp.y] != 0)
				kind = out[temp.x][temp.y];

			if(visit[temp.x][temp.y] == 0)
			{
				visit[temp.x][temp.y] = 1;
				vc.push_back(temp);
				dq.push_back(temp);
			}
		}
	}

	if(kind == 0)
		kind = nowkind ++;

	for(i = 0; i < vc.size(); i ++)
	{
		now = vc[i];
		out[now.x][now.y] = kind;
	}
}
int main()
{
    freopen("B-large.in.txt", "r", stdin);
    freopen("B-large.txt", "w", stdout);
	int i,j, Test = 1;
	int t;
	scanf("%d",&t);

	while(t --)
	{
		scanf("%d %d",&r,&c);
		for(i = 0; i < r; i ++)
		{
			for(j = 0; j < c; j ++)
			{
				scanf("%d", &mat[i][j]);
				visit[i][j] = 0;
				out[i][j] = 0;
			}
		}

		nowkind = 'a';
		for(i = 0; i < r; i ++)
		{
			for(j = 0; j < c ; j ++)
			{
				if(out[i][j] == 0)
				{
					now.x = i;
					now.y = j;
					bfs();
				}
			}
		}

		printf("Case #%d:\n",Test ++);
		for(i = 0; i < r; i ++)
		{
			for(j = 0; j < c; j ++)
			{
				if(j)
					printf(" ");
				printf("%c", out[i][j]);
			}
			printf("\n");
		}
	}
	return 0;
}
