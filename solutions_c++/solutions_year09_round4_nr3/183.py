#include <cstdio>
#include <cstring>
#define MAXN 110
#define MAXM 50000
struct edge
{
    int to, next;
}e[MAXM];
int tail;
int n, m, b[MAXN][MAXN];
int mx[MAXN], my[MAXN], v[MAXN], a[MAXN];

void add(int x, int y, int &tail) {e[++tail].to = y; e[tail].next = a[x]; a[x] = tail;}

int path(int now, int k)
{
	for (int i = a[now]; i >= 0; i = e[i].next)
		if (v[e[i].to] != k)
		{
			v[e[i].to] = k;
			if (my[e[i].to] == -1 || path(my[e[i].to], k))
			{
				mx[now] = e[i].to;
				my[e[i].to] = now;
				return 1;
			}
		}
	return 0;
}

int maxmatch()
{
	int ans = 0;
	memset(mx, -1, sizeof(mx));
	memset(my, -1, sizeof(my));
	memset(v, 0, sizeof(v));
	for (int i = 1; i <= n; i++)
		if (mx[i] == -1) ans += path(i, i);
	return ans;
}

int main() {
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	int cases;
	scanf("%d", &cases);
	for (int cc = 1; cc <= cases; cc++) {
		scanf("%d%d", &n, &m);
		memset(a, -1, sizeof(a));
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= m; j++) {
				scanf("%d", &b[i][j]);
			}
		}
		bool ok; tail = -1;
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= n; j++) {
				ok = 1;
				for (int k = 1; k <= m; k++)
					if (b[i][k] <= b[j][k]) {
						ok = 0;
						break;
					}
				if (ok) add(i, j, tail);
			}
		}
		printf("Case #%d: %d\n", cc, n - maxmatch());
	}
	fclose(stdin); fclose(stdout);
	return 0;
}