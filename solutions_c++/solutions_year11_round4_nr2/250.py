#include <cstdio>
#include <cmath>

const int MaxR = 505;
int r, c, d, num[MaxR][MaxR];

void input()
{
	scanf("%d%d%d", &r, &c, &d);
	for (int i = 1; i <= r; ++ i) {
		char text[MaxR];
		scanf("%s", text);
		for (int j = 0; j < c; ++ j) num[i][j + 1] = text[j] - '0';
	}
}

bool check(int x0, int x1, int y0, int y1)
{
	double cx = (x0 + x1 + 1) / 2.0, cy = (y0 + y1 + 1) / 2.0;
	double totalx = 0, totaly = 0;
	for (int i = x0; i <= x1; ++ i)
		for (int j = y0; j <= y1; ++ j) {
			if ((i == x0 && (j == y0 || j == y1)) || (i == x1 && (j == y0 || j == y1)))
				continue;
			totalx += (i + 0.5 - cx) * num[i][j];
			totaly += (j + 0.5 - cy) * num[i][j];
		}
	return fabs(totalx) < 1e-8 && fabs(totaly) < 1e-8;
}

void solve()
{
	int min = r < c ? r : c, result = 0;
	for (int k = 3; k <= min; ++ k) {
		for (int x0 = 1, x1 = k; x1 <= r; ++ x0, ++ x1)
			for (int y0 = 1, y1 = k; y1 <= c; ++ y0, ++ y1) {
				if (check(x0, x1, y0, y1)) result = k;
			}
	}
	if (result) {
		printf("%d\n", result);
	} else {
		printf("IMPOSSIBLE\n");
	}
}

int main()
{
	int testCases;
	scanf("%d\n", &testCases);
	for (int t = 1; t <= testCases; ++ t) {
		input();
		printf("Case #%d: ", t);
		solve();
	}
	return 0;
}
