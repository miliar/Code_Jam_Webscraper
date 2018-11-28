#include <iostream>
#include <vector>
#include <string>
#include <cassert>
using namespace std;

int a[111][111];
int comp[111][111];
bool u[111][111];
int col[111111];

const int maxc = 11111;
//North, West, East, South.
int dx[] = {-1, 0, 0, 1};
int dy[] = {0, -1, 1, 0};

int dfs(int x, int y)
{
	if(comp[x][y]) return comp[x][y];
	int bx = -1, by, bb = maxc + 20;
	for(int i = 0; i < 4; ++i)
	{
		int nx = x + dx[i], ny = y + dy[i];
		if(a[nx][ny] >= a[x][y]) continue;
		
		if(a[nx][ny] < bb)
			bb = a[nx][ny],
			bx = nx, by = ny;
	}
	if(bx == -1)
	{
		cerr << x << " " << y << endl;
	} else
		comp[x][y] = dfs(bx, by);
	return comp[x][y];
}

vector< vector<int> > g;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t; scanf("%d", &t);
	for(int z = 1; z <= t; ++z)
	{
		int n, m; scanf("%d%d", &n, &m);
		for(int i = 0; i < n + 2; ++i)
			for(int j = 0; j < m + 2; ++j)
				a[i][j] = maxc;
		memset(comp, 0, sizeof comp);
		for(int i = 1; i <= n; ++i)
			for(int j = 1; j <= m; ++j)
			{
				scanf("%d", &a[i][j]);
			}
		int cc = 0;
		for(int i = 1; i <= n; ++i)
			for(int j = 1; j <= m; ++j)
				if((a[i][j] <= a[i-1][j] && a[i][j] <= a[i][j-1] && a[i][j] <= a[i+1][j] && a[i][j] <= a[i][j+1]))
				{
					comp[i][j] = ++cc;
				}
		for(int i = 1; i <= n; ++i)
			for(int j = 1; j <= m; ++j) if(!comp[i][j])
				dfs(i, j);
		/*for(int i = 0; i < n + 2; ++i)
		{
			for(int j = 0; j < m + 2; ++j)
				cerr << comp[i][j] << " ";
			cerr << endl;
		}
		*/
		cc++;
		g.clear();
		g.resize(cc);
		
		for(int i = 1; i <= n; ++i)
			for(int j = 1; j <= m; ++j)
			{
				for(int k = 0; k < 4; ++k)
				{
					int nx = i + dx[k], ny = j + dy[k];
					if(comp[nx][ny])
						g[comp[i][j]].push_back(comp[nx][ny]);
				}
			}
		memset(col, -1, sizeof col);
		vector<bool> used(26, 0);
		for(int i = 1; i <= n; ++i)
			for(int j = 1; j <= m; ++j) if(col[comp[i][j]] == -1)
			{
				vector<bool> free(26, true);
				for(int k = 0; k < 26; ++k)
					if(used[k])
						free[k] = false;
				for(int k = 0; k < g[comp[i][j]].size(); ++k)
					if(col[k] != -1)
						free[col[k]] = false;
				int what = -1;
				for(int k = 0; k < 26; ++k)
					if(free[k])
					{
						what = k;
						break;
					}
				col[comp[i][j]] = what;
				used[what] = true;
				assert(what != -1);
			}
		printf("Case #%d:\n", z);
		for(int i = 1; i <= n; ++i)
		{
			for(int j = 1; j <= m; ++j)
			{
				if(j != 1) printf(" ");
				printf("%c", char(col[comp[i][j]] + 'a'));
			}
			printf("\n");
		}
	}
	return 0;
}