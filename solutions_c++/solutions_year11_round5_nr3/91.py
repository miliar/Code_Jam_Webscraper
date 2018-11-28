#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

#define sz(a) int((a).size())
#define all(X) (X).begin(), (X).end()
typedef vector<int> vi;
typedef vector<string> vs;
typedef long long ll;

char buff[10][10];
int n, m;
int ind[10][10];
int xx, yy;

bool dfs(int x, int y, int msk, int c)
{
	if (ind[x][y] == c) {
		if (!(xx == x && yy == y)) {
			return false;
		}
		return true;
	}
	if (ind[x][y] == -1) {
		ind[x][y] = c;
		int ii = x * m + y;
		if (buff[x][y] == '-') {
			if (msk & (1 << ii)) {
				if (!dfs(x, (y + 1) % m, msk, c)) {
					return false;
				}
			}
			else {
				if (!dfs(x, (y - 1 + m) % m, msk, c)) {
					return false;
				}
			}
		}
		else if (buff[x][y] == '|') {
			if (msk & (1 << ii)) {
				if (!dfs((x + 1) % n, y, msk, c)) {
					return false;
				}
			}
			else {
				if (!dfs((x + n - 1) % n, y, msk, c)) {
					return false;
				}
			}
		}
		else if (buff[x][y] == '/') {
			if (msk & (1 << ii)) {
				if (!dfs((x + 1) % n, (y + m - 1) % m, msk, c)) {
					return false;
				}
			}
			else {
				if (!dfs((x + n - 1) % n, (y + 1) % m, msk, c)) {
					return false;
				}
			}
		}
		else {
			if (msk & (1 << ii)) {
				if (!dfs((x + 1) % n, (y + 1) % m, msk, c)) {
					return false;
				}
			}
			else {
				if (!dfs((x + n - 1) % n, (y + m - 1) % m, msk, c)) {
					return false;
				}
			}
		}
		return true;
	}
	else {
		return false;
	}
}

bool isok(int msk)
{
	memset(ind, -1, sizeof(ind));
	int c = 0;
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			if (ind[i][j] == -1) {
				xx = i, yy = j;
				if (!dfs(i, j, msk, c)) {
					return false;
				}
				++c;
			}
		}
	}
	return true;
}

int run()
{
	scanf("%d %d", &n, &m);
	for (int i = 0; i < n; ++i) {
		scanf("%s", buff[i]);
	}
	int ret = 0;
	for (int i = 0; i < (1 << (n * m)); ++i) {
		if (isok(i)) {
			++ret;
		}
	}
	return ret;
}

int main()
{
	freopen("C0.in", "r", stdin);
	freopen("C0.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i) {
		printf("Case #%d: %d\n", i, run());
	}
	return 0;
}