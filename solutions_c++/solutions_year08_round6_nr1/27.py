#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int n, m, q;
int gx[1000], gy[1000];
int bx[1000], by[1000];

inline bool within(int x1, int y1, int x2, int y2, int x, int y) {
	return min(x1, x2) <= x && x <= max(x1, x2) && min(y1, y2) <= y && y <= max(y1, y2);
}

int check(int x, int y)
{
	int i, j;
	for (i = 0; i < n; i++)
		for (j = i + 1; j < n; j++)
			if (within(gx[i], gy[i], gx[j], gy[j], x, y)) return 0;
	for (i = 0; i < n; i++)
		for (j = 0; j < m; j++)
			if (within(gx[i], gy[i], x, y, bx[j], by[j])) return 1;
	return 2;
}

int main()
{
	freopen("alarge.in", "r", stdin);
	freopen("alarge.out", "w", stdout);

	int i, j, k, x, y, z, testcase;
	char str[100];

	scanf("%d", &testcase);

	for (z = 1; z <= testcase; z++) {
		fprintf(stderr, "%d\n", z);
		scanf("%d", &k);
		n = m = 0;
		for (i = 0; i < k; i++) {
			scanf("%d%d%s", &x, &y, str);
			if (!strcmp(str, "BIRD")) {
				gx[n] = x;
				gy[n] = y;
				n++;
			} else {
				bx[m] = x;
				by[m] = y;
				m++;
				scanf("%s", str);
			}
		}

		printf("Case #%d:\n", z);
		scanf("%d", &q);
		for (i = 0; i < q; i++) {
			scanf("%d%d", &x, &y);
			j = check(x, y);
			if (j == 0) printf("BIRD\n");
			else if (j == 1) printf("NOT BIRD\n");
			else printf("UNKNOWN\n");
		}
	}

	return 0;
}
