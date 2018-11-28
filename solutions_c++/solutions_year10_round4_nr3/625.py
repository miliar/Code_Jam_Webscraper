#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

static inline bool
run(char (*now)[104], char (*next)[104])
{
	bool ret = false;
	for (int i = 1; i <= 100; i++)
		for (int j = 1; j <= 100; j++) {
			char a = now[i][j], b = now[i-1][j], c = now[i][j-1],
			    &d = next[i][j];
			if (a == 1 && b == 0 && c == 0)
				d = 0;
			else if (a == 0 && b == 1 && c == 1)
				d = 1;
			else
				d = a;
			if (a)
				ret = true;
		}
	return ret;
}

static int
doit()
{
	static char a[104][104], b[104][104];
	int r;
	scanf("%d", &r);
	memset(a, 0, sizeof(a));
	for (int i = 0; i < r; i++) {
		int x1, y1, x2, y2;
		scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
		for (int x = x1; x <= x2; x++)
			for (int y = y1; y <= y2; y++)
				a[x][y] = 1;
	}
	int all = 0;
	char (*now)[104] = a, (*next)[104] = b;
	while (run(now, next)) {
		all++;
		swap(next, now);
	}
	return all;
}

int
main()
{
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; i++)
		printf("Case #%d: %d\n", i+1, doit());
	return 0;
}
