#include <cstdio>
#include <algorithm>
#define abs(x) (((x) > 0)? (x) : (-(x)))
using namespace std;

int det(int x1, int y1, int x2, int y2)
{
	return x1 * y2 - x2 * y1;
}

int main()
{
	int x1, x2, y1, y2, a, cases, n, m, t = 0;
	bool flag;
	freopen("D:\\b.in", "r", stdin);
	freopen("D:\\b.out", "w", stdout);
	//freopen("in", "r", stdin);
	scanf("%d", &cases);
	while (cases--)
	{
		printf("Case #%d: ", ++t);
		scanf("%d%d%d", &n, &m, &a);
		flag = false;
		for (x1 = 0; !flag && x1 <= n; x1++)
			for (y1 = 0; !flag && y1 <= m; y1++)
				for (x2 = 0; !flag && x2 <= n; x2++)
					for (y2 = 0; !flag && y2 <= m; y2++)
						if (abs(det(x1, y1, x2, y2)) == a)
						{
							flag = true;
							printf("0 0 %d %d %d %d\n", x1, y1, x2, y2);
						}
		if (!flag) puts("IMPOSSIBLE");
	}
	return 0;
}