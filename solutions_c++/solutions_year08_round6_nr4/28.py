#include <cstdio>
#include <cstring>

int n, m;
bool g[50][50], gg[50][50];
int map[50];
bool v[50];

bool check()
{
	int i, j;
	for (i = 0; i < m; i++)
		for (j = i + 1; j < m; j++)
			if (gg[i][j] != g[map[i]][map[j]]) return false;
	return true;
}

bool search(int now)
{
	if (now == m) return check();
	int i;
	for (i = 0; i < n; i++)
		if (!v[i]) {
			map[now] = i;
			v[i] = true;
			if (search(now + 1)) return true;
			v[i] = false;
		}
	return false;
}

int main()
{
	freopen("dsmall.in", "r", stdin);
	freopen("dsmall.out", "w", stdout);

	int i, j, k, z, testcase;

	scanf("%d", &testcase);
	for (z = 1; z <= testcase; z++) {
		memset(g, false, sizeof(g));
		memset(gg, false, sizeof(gg));
		scanf("%d", &n);
		for (i = 1; i < n; i++) {
			scanf("%d%d", &j, &k);
			j--, k--;
			g[j][k] = g[k][j] = true;
		}
		scanf("%d", &m);
		for (i = 1; i < m; i++) {
			scanf("%d%d", &j, &k);
			j--, k--;
			gg[j][k] = gg[k][j] = true;
		}
		printf("Case #%d: ", z);
		memset(v, false, sizeof(v));
		if (search(0)) printf("YES\n");
		else printf("NO\n");
	}

	return 0;
}
