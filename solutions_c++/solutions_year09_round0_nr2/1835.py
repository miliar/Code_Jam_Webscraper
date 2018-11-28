#include <iostream>
#include <cstring>
#include <vector>
#include <algorithm>
#include <queue>
#include <climits>

using namespace std;
const int MAX = 110;
//int move[2][4] = {{0, -1, 1, 0}, {-1, 0, 0, 1}};
int move[2][4] = {{-1, 0, 0, 1}, {0, -1, 1, 0}};
int n, m;
int area[MAX][MAX];
int p[MAX][MAX];

inline int findMin(int x, int y)
{
	int rt = INT_MAX;
	for(int i = 0; i < 4; i++)
	{
		int tx = x + move[0][i], ty = y + move[1][i];
		if(tx >= 0 && tx < n && ty >= 0 && ty < m) rt = min(rt, area[tx][ty]);
	}
	return rt;
}

int dfs(int x, int y)
{
	if(p[x][y]) return p[x][y];
	int h = findMin(x, y);
	for(int i = 0; i < 4; i++)
	{
		int tx = x + move[0][i], ty = y + move[1][i];
		if(tx >= 0 && tx < n && ty >= 0 && ty < m && area[tx][ty] == h)
				return (p[x][y] = dfs(tx, ty));
	}
}

void buildGraph()
{
	memset(p, 0, sizeof(p));

	int cnt = 1;
	for(int i = 0; i < n; i++)
		for(int j = 0; j < m; j++)
			if(findMin(i, j) >= area[i][j]) p[i][j] = cnt++;
}

int main()
{
	freopen("B-small-attempt3.in", "r", stdin);
	freopen("B-small-attempt3.out", "w", stdout);
//	freopen("B-small-attempt1.out", "w", stdout);
	int tcase;
	cin >> tcase;
	for(int tc = 1; tc <= tcase; tc++)
	{
		memset(area, 1, sizeof(area));
		memset(p, 0, sizeof(p));
		cin >> n >> m;
		for(int i = 0; i < n; i++)
			for(int j = 0; j < m; j++)
				cin >> area[i][j];
		buildGraph();
		for(int i = 0; i < n; i++)
			for(int j = 0; j < m; j++)
				p[i][j] = dfs(i, j);

		char label[100], ch = 'a';
		memset(label, 0, sizeof(label));
		cout << "Case #" << tc << ":" << endl;
		for(int i = 0; i < n; i++)
			for(int j = 0; j < m; j++)
			{
				if(label[p[i][j]] == 0) label[p[i][j]] = ch++;
				cout << label[p[i][j]];
				if(j != m - 1) cout << " ";
				else cout << endl;
			}
	}
	return 0;
}
