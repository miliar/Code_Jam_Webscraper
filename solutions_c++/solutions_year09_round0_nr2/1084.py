#include<cstdio>
#include<cstring>
#include<algorithm>
#include<map>
using namespace std;
map<int, char> print;
int n ,m;
struct gridtype
{
	pair<int,int> posi;
	int height;
} grid[10000];
int fa[100][100];
char out[100][100];
int al[100][100];
int dx[4] = {-1,0,0,1};
int dy[4] = {0,-1,1,0};
bool cmp(gridtype a, gridtype b)
{
	return a.height < b.height;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	int ca;
	scanf("%d" , &ca);
	for (int cases = 1; cases <= ca; ++cases)
	{
		scanf("%d%d" , &n,  &m);
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < m; ++j)
			{
				int altitude;
				scanf("%d" , &altitude);
				grid[i * m + j].posi = make_pair(i,j);
				grid[i * m + j].height = altitude;
				al[i][j] = altitude;
			}
		sort( grid, grid + n * m , cmp);
		for (int i = 0; i < n * m; ++i)
		{
			int xx = grid[i].posi.first;
			int yy = grid[i].posi.second;
			int minimum = grid[i].height;
			int mind = -1;
			for (int d = 0; d < 4; ++d)
			{
				int x = xx + dx[d];
				int y = yy + dy[d];
				if (x < 0 || x >= n || y < 0 || y >= m) continue;
				if (al[x][y] < minimum)
				{
					minimum = al[x][y];
					mind = d;
				}
			}
			if (mind == -1) fa[xx][yy] = xx * m + yy;
			else
			{
				int x = xx + dx[mind];
				int y = yy + dy[mind];
				fa[xx][yy] = fa[x][y];
			}
		}
		char now = 'a';
		print.clear();
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < m; ++j)
			{
				if (print.find(fa[i][j]) == print.end()) print[fa[i][j]] = now++;
				out[i][j] = print[fa[i][j]];
			}
		printf("Case #%d:\n" , cases);
		for (int i = 0; i < n; ++i)
		{
			for (int j = 0; j < m - 1; ++j) printf("%c " , out[i][j]);
			printf("%c\n", out[i][m - 1]);
		}
	}
}
