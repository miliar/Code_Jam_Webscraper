#include<iostream>

using namespace std;

int main()
{
	freopen("a.txt", "r", stdin);
	freopen("b.txt", "w", stdout);
	int caseID = 1;
	int t;
	scanf("%d", &t);
	int n, m, a;
	while (caseID <= t)
	{
		printf("Case #%d: ", caseID++);
		scanf("%d %d %d", &n, &m, &a);
		bool flag = 0;
		int x1, x2, y1, y2;
		for (x1 = 0; x1 <= n; x1++)
		{
			for (x2 = 0; x2 <= n; x2++)
			{
				for (y1 = 0; y1 <= m; y1++)
				{
					for (y2 = 0; y2 <= m; y2++)
					{
						if (x1 * y2 - x2 * y1 == a && !(x1 == x2 && y1 == y2)) flag = 1;
						if (flag) break;
					}
					if (flag) break;
				}
				if (flag) break;
			}
			if (flag) break;
		}
		if (!flag) printf("IMPOSSIBLE\n");
		else printf("0 0 %d %d %d %d\n", x1, y1, x2, y2);
	}
	return 0;
}