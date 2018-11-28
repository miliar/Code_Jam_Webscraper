#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <map>

using namespace std;

int height[101][101];
int t,h,w;

int dir[][2] = {{-1,0}, {0,-1}, {0,1}, {1,0}};

bool valid(int x, int y)
{
	return (x >= 0)&&(y >= 0)&&(x < h)&&(y < w);
}

struct Point
{
	int x, y;
	Point(){};
	Point(int a, int b){x = a; y = b;};
};

bool eq(const Point & p1, const Point & p2)
{
	return p1.x == p2.x && p1.y == p2.y;
}

Point parent[101][101];
int rank[101][101];
char color[101][101];

Point find(Point p1)
{
	Point p2, p3;
	
	p2 = p1;
	while(!eq(p2, parent[p2.x][p2.y]))
		p2 = parent[p2.x][p2.y];
	while(!eq(p1, p2))
	{
		p3 = parent[p1.x][p1.y];
		parent[p1.x][p1.y] = p2;
		p1 = p3;
	}
	return p2;
}

void merge(Point & p1, Point & p2)
{
	Point pp1 = find(p1);
	Point pp2 = find(p2);

	if(pp1.x == pp2.x && pp1.y == pp2.y)
	{
		return;
	}
	else
	{
		if(rank[pp1.x][pp1.y] > rank[pp2.x][pp2.y])
		{
			parent[pp2.x][pp2.y] = pp1;
			rank[pp1.x][pp1.y] += rank[pp2.x][pp2.y];
		}
		else
		{
			parent[pp1.x][pp1.y] = pp2;
			rank[pp2.x][pp2.y] += rank[pp1.x][pp1.y];
		}
	}
}


int main()
{
	int i,j,k;
	int x,y;

	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	scanf("%d", &t);
	for (int cas = 1; cas <= t; cas++)
	{
		scanf("%d%d", &h, &w);
		for (i = 0; i < h; i++)
		{
			for (j = 0; j < w; j++)
			{
				scanf("%d", &height[i][j]);
				rank[i][j] = 1;
				parent[i][j] = Point(i, j);
				color[i][j] = 0;
			}
		}

		for (i = 0; i < h; i++)
		{
			for (j = 0; j < w; j++)
			{
				int ti, tj;
				ti = i;
				tj = j;
				for(k = 0; k < 4; k++)
				{
					x = i + dir[k][0];
					y = j + dir[k][1];
					if(valid(x, y) && height[x][y] < height[ti][tj])
					{
						ti = x; tj = y;
					}
				}
				merge(Point(i, j), Point(ti, tj));
			}
		}

		char current = 'a';
		for (i = 0; i < h; i++)
		{
			for (j = 0; j < w; j++)
			{
				Point p = find(Point(i, j));
				if(color[p.x][p.y] == 0)
					color[p.x][p.y] = current++;
				color[i][j] = color[p.x][p.y];
			}
		}
		printf("Case #%d:\n", cas);
		for (i = 0; i < h; i++)
		{
			for (j = 0; j < w; j++)
			{
				printf("%c", color[i][j]);
				if(j == (w - 1))
					printf("\n");
				else
					printf(" ");
			}
		}
	}
	return 0;
}