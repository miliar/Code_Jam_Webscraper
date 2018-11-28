#include <cstdio>
#include <algorithm>

using namespace std;

enum {OR, AND, SIZE = 32};

static int	type[SIZE], now[SIZE], canch[SIZE];

static int
eval(int r, int in)
{
	if (r > in) // leaf
		return (now[r]);
	int a = eval(2 * r, in),
	    b = eval(2 * r + 1, in);
	if (now[r] == AND)
		return (a & b);
	return (a | b);
}

static void
doit()
{
	int m, v;
	scanf("%d%d", &m, &v);
	int in = (m - 1) / 2;
	for (int i = 1; i <= in; i++)
		scanf("%d%d", &type[i], &canch[i]);
	for (int i = in + 1; i <= m; i++)
		scanf("%d", &type[i]);

	int ans = SIZE;
	for (int i = 0; i < (1 << in); i++) {
		int ch = 0;
		for (int k = 1; k <= m; k++)
			now[k] = type[k];
		bool again = false;
		for (int k = 0; k < in; k++)
			if (i & (1 << k)) {
				if (!canch[k + 1]) {
					again = true;
					break;
				}
				ch++;
				now[k + 1] ^= 1;
			}
		if (again)
			continue;
		if (eval(1, in) == v) {
			if (ch < ans)
				ans = ch;
		}
	}
	if (ans == SIZE)
		printf("IMPOSSIBLE\n");
	else
		printf("%d\n", ans);
}

int
main()
{
	int n;
	scanf("%d", &n);
	for (int i = 1; i <= n; i++) {
		printf("Case #%d: ", i);
		doit();
	}
	return (0);
}
