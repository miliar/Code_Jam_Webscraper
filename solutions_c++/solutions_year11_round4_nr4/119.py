#include <iostream>
#include <queue>
#include <cstring>
#include <cstdio>

using namespace std;

const int MXN = 37;

int n, m;
int ans1, ans2;
int tmp1, tmp2;
bool g[MXN][MXN];
int d[MXN];
int id[MXN];

void dfs(int u)
{
	if (id[1] == 1) {
		tmp1 = tmp2 = 0;
		for (int i = 0; i < n; ++i) {
			if (id[i] == 1) ++tmp2;
			if (id[i] == 2) ++tmp1;
		}
		if (tmp1 < ans1) {
			ans1 = tmp1;
			ans2 = tmp2;
		} else if (tmp1 == ans1 && tmp2 > ans2) {
			ans2 = tmp2;
		}
		return;
	}
	int tid[MXN];
	for (int i = 0; i < n; ++i)
		if (g[u][i] && d[u] == d[i] + 1 && id[i] == 1) {
			memmove(tid, id, sizeof tid);
			id[i] = 2;
			for (int j = 0; j < n; ++j)
				if (g[i][j] && id[j] == 0) id[j] = 1;
			dfs(i);
			memmove(id, tid, sizeof id);
		}
}

int main()
{
	int T;
	scanf("%d", &T);
	int numCase = 0;
	while (T--) {
		scanf("%d%d", &n, &m);
		memset(g, 0, sizeof g);
		memset(id, 0, sizeof id);
		while (m--) {
			int u, v;
			scanf("%d,%d", &u, &v);
			g[u][v] = g[v][u] = true;
		}
		
		queue<int> q;
		memset(d, -1, sizeof d);
		d[1] = 0;
		q.push(1);
		while (!q.empty()) {
			int u = q.front();
			q.pop();

			for (int i = 0; i < n; ++i)
				if (g[u][i] && d[i] == -1) {
					d[i] = d[u] + 1;
					q.push(i);
				}
		}

		ans1 = ~0U >> 1;
		ans2 = 0;
		id[0] = 2;
		for (int i = 0; i < n; ++i)
			if (g[0][i]) id[i] = 1;
		dfs(0);
		printf("Case #%d: %d %d\n", ++numCase, ans1 - 1, ans2);
	}
}
