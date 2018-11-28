#include <cstdio>
#include <algorithm>
#include <map>
#include <vector>

using namespace std;

enum {SIZE = 105, INF = 987654321};

bool visited[SIZE][SIZE];
int grid[SIZE][SIZE];
int m, n;
int ans[SIZE][SIZE], c;
int dx[] = {-1, 0, 0, 1};
int dy[] = {0, -1, 1, 0};

void dfs(int x, int y)
{
	if(x >= 0 && y >= 0 && x < m && y < n && !visited[x][y]) {
		visited[x][y] = true;
		ans[x][y] = c;
		int low = grid[x][y], lowx, lowy;
		for(int i = 0; i < 4; i++) {
			int nx = x + dx[i], ny = y + dy[i];
			if(nx >= 0 && ny >= 0 && nx < m && ny < n && grid[nx][ny] < low) {
				low = grid[nx][ny];
				lowx = nx;
				lowy = ny;
			}
		}
		if(low < grid[x][y]) {
			dfs(lowx, lowy);
			ans[x][y] = min(ans[x][y], ans[lowx][lowy]);
		}
		else
			c++;
	}
}

void process(int no)
{
	map<int, char> table;
	vector<int> anss;
	char v = 'a';
	
	scanf("%d %d", &m, &n);

	for(int i = 0; i < m; i++)
		for(int j = 0; j < n; j++)
			scanf("%d", &grid[i][j]);
	
	for(int i = 0; i < m; i++)
		for(int j = 0; j < n; j++) {
			visited[i][j] = false;
			ans[i][j] = 'z' + 1;
		}

	c = 0;

	for(int i = 0; i < m; i++)
		for(int j = 0; j < n; j++)
			dfs(i, j);

	for(int i = 0; i < m; i++)
		for(int j = 0; j < n; j++)
			anss.push_back(ans[i][j]);

	sort(anss.begin(), anss.end());
	
	for(int i = 0; i < anss.size(); i++)
		if(!table.count(anss[i]))
			table[anss[i]] = v++;

	for(int i = 0; i < m; i++)
		for(int j = 0; j < n; j++)
			ans[i][j] = table[ans[i][j]];
	
	printf("Case #%d:\n", no);
		
	for(int i = 0; i < m; i++)
		for(int j = 0; j < n; j++)
			if(j == n - 1)
				printf("%c\n", ans[i][j]);
			else
				printf("%c ", ans[i][j]);
}

int main()
{
	int tc;
	
	scanf("%d", &tc);

	for(int i = 0; i < tc; i++)
		process(i + 1);
	
	return 0;
}
