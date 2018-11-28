#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
#include <vector>
#include <string>
//#include <cmath>
#include <map>
#include <set>

using namespace std;

int n, k, cur, mn;
int p[100][25];
bool g[100][100];
int col[100];

void read_data()
{
	scanf("%d%d", &n, &k);
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < k; ++j)
			scanf("%d", &p[i][j]);
}

void run(int u) {
	if (cur >= mn) return;
	if (u == n) { if (cur < mn) mn = cur; return; }

	for (int c = 0; c < cur; ++c) {
		bool ok = true;

		for (int v = 0; v < u; ++v)
			if (col[v] == c && g[v][u]) { ok = false; break; }

		if (ok) { col[u] = c; run(u+1); }
	}

	col[u] = cur++; run(u+1); --cur;
}

void solve()
{
	memset(g, 0, sizeof(g)); mn = n; cur = 1;

	for (int i = 0; i < n; ++i)
		for (int j = i+1; j < n; ++j) {
			g[i][j] = false;
			for (int l = 0; l < k-1; ++l)
				if ((p[i][l] == p[j][l]) || (p[i][l+1] == p[j][l+1]) || (p[i][l]>p[j][l] && p[i][l+1]<p[j][l+1]) || (p[i][l]<p[j][l] && p[i][l+1]>p[j][l+1])) {
					g[i][j] = true; break;
				}

			g[j][i] = g[i][j];
		}

	run(0);
	printf("%d\n", mn);
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		printf("Case #%d: ", t);
//		fprintf(stderr, "%d\n", t);
		read_data();
		solve();
	}

	return 0;
}
