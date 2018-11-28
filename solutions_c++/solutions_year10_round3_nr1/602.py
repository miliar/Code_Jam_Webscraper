#include <iostream>

using namespace std;

int x[1005];
int y[1005];

int main()
{
	freopen("a.in", "rt", stdin);
	freopen("a.out", "wt", stdout);
	int i, j, n, tc, nc, res, stat1, stat2;
	scanf("%d", &tc);
	for (nc = 1; nc <= tc; nc++) {
		res = 0;
		scanf("%d", &n);
		for (i = 0; i < n; i++) {
			scanf("%d%d", &x[i], &y[i]);
		}
		for (i = 0; i < n; i++) {
			for (j = i+1; j < n; j++) {
				stat1 = (int)(x[i] < x[j]);
				stat2 = (int)(y[i] < y[j]);
				res += (stat1 ^ stat2);
			}
		}
		printf("Case #%d: %d\n", nc, res);
	}
}
