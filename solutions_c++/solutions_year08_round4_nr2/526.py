#include <cstdio>

int n, m, a;
void solve (int t)
{
	int x1, y1, x2, y2, u;
	for (x1 = 0; x1 <= n; x1++)
		for (y1 = 0; y1 <= m; y1++)
			for (x2 = 0; x2 <= n; x2++)
				for (y2 = 0; y2 <= m; y2++){
					u = x1 * y2 - x2 * y1;
					if (u == a || u == -a) {
						printf ("Case #%d: 0 0 %d %d %d %d\n", t, x1, y1, x2, y2);
						return ;
					}
				}
	printf ("Case #%d: IMPOSSIBLE\n", t);
}
int main ()
{
	int c;
//    freopen ("B-small-attempt1.in", "r", stdin);
//	freopen ("out.txt", "w", stdout);
	scanf ("%d", &c);
	for (int t = 1; t <= c; t++){
		scanf ("%d%d%d", &n, &m, &a);
		solve (t);
	}
}
