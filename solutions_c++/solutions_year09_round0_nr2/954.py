#include <algorithm>
#include <iostream>
#include <cstring>
#include <iomanip>
#include <cstdio>
#include <string>
#include <vector>
#include <map>
#include <set>

using namespace std;

int N, H, W, cur;
int f[102][102];
int res[102][102];

void read_data()
{
	cin >> H >> W;

	for (int i = 0; i <= H+1; ++i)
		for (int j = 0; j <= W+1; ++j)
			f[i][j] = 20000;

	for (int i = 1; i <= H; ++i)
		for (int j = 1; j <= W; ++j)
			cin >> f[i][j];
}

void dfs(int i, int j) {
	if (res[i][j] != -1) return;

	int ht = 20000;
	if (ht > f[i-1][j]) ht = f[i-1][j];
	if (ht > f[i][j-1]) ht = f[i][j-1];
	if (ht > f[i][j+1]) ht = f[i][j+1];
	if (ht > f[i+1][j]) ht = f[i+1][j];

	if (ht >= f[i][j]) { res[i][j] = cur++; return; }
	if (ht == f[i-1][j]) { dfs(i-1, j); res[i][j] = res[i-1][j]; return; }
	if (ht == f[i][j-1]) { dfs(i, j-1); res[i][j] = res[i][j-1]; return; }
	if (ht == f[i][j+1]) { dfs(i, j+1); res[i][j] = res[i][j+1]; return; }
	if (ht == f[i+1][j]) { dfs(i+1, j); res[i][j] = res[i+1][j]; return; }
}

void solve()
{
	cur = 0;
	memset(res, -1, sizeof(res));
	for (int i = 1; i <= H; ++i)
		for (int j = 1; j <= W; ++j)
			if (res[i][j] == -1) dfs(i, j);

	char q[26]; cur = 'a';
	memset(q, '0', sizeof(q));
	for (int i = 1; i <= H; ++i)
		for (int j = 1; j <= W; ++j)
			if (q[res[i][j]] == '0') q[res[i][j]] = cur++;

	for (int i = 1; i <= H; ++i) {
		for (int j = 1; j <= W; ++j)
			cout << q[res[i][j]] << " ";

		cout << endl;
	}
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	cin >> N;

	for (int i = 0; i < N; ++i) {
		cout << "Case #" << i+1 << ":" << endl;
		read_data();
		solve();
	}

	return 0;
}
