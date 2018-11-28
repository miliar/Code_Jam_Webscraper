#include <cstdio>
#include <cstring>
#include <set>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;

int T, H, W;
int a[105][105];
int f[105][105];
int dir[][2] = { { 1, 0 }, { 0, 1 }, { 0, -1 }, { -1, 0 } };

int dfs(int x, int y)
{
	int flag = -1;
	int res = a[x][y];
	for (int i = 0; i < 4; ++i)  {
		int newx = x + dir[i][0];
		int newy = y + dir[i][1];
		if (newx < 0 || newx >= H || newy < 0 || newy >= W)
			continue;
		if (a[newx][newy] <= res) {
			flag = i;
			res = a[newx][newy];
		}
	}
	if (flag != -1 && res != a[x][y]) {
		return f[x][y] = dfs(x + dir[flag][0], y + dir[flag][1]);
	}
	else
		return f[x][y] = x * W + y;
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		scanf("%d %d", &H, &W);
		for (int i = 0; i < H; ++i)
			for (int j = 0; j < W; ++j)
				scanf("%d", &a[i][j]);
		memset(f, 0xff, sizeof(f));
		map<int, int> m;
		for (int i = 0; i < H; ++i) {
			for (int j = 0; j < W; ++j) {
				if (f[i][j] == -1) {
					dfs(i, j);
				}
			}
		}
		vector<int> v;
		for (int i = 0; i < H; ++i) {
			for (int j = 0; j < W; ++j) {
				if (m.count(f[i][j]))
					continue;
				m[f[i][j]] = i * W + j;
				v.push_back(i * W + j);
			}
		}
		sort(v.begin(), v.end());
		map<int, char> m2;
		for (int i = 0; i < v.size(); ++i)
			m2[v[i]] = (char) (i + 'a');
		printf("Case #%d:\n", t);
		for (int i = 0; i < H; ++i) {
			for (int j = 0; j < W; ++j) {
				if (j)
					putchar(' ');
				putchar(m2[m[f[i][j]]]);
			}
			putchar('\n');
		}
	}
	return 0;
}