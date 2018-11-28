#include <iostream>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;

int n, t, r, x1, x2, y1, y2;
bool a[2][310][310];

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	scanf("%d", &t);
	for (int tt = 1; tt <= t; tt++)
	{
		printf("Case #%d: ", tt);
		scanf("%d", &r);
		memset(a, 0, sizeof(a));
		for (int k = 0; k < r; k++)
		{
			scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
			x1 += 100; y1 += 100; x2 += 100; y2 += 100;
			for (int i = x1; i <= x2; i++)
				for (int j = y1; j <= y2; j++)
					a[0][i][j] = 1;
		}
		int ans = 0;
		while (1)
		{
			int k = (ans & 1);
			bool br = true;
			for (int i = 1; i < 305; i++)
				for (int j = 1; j < 305; j++)
				{
					a[1 - k][i][j] = a[k][i][j];
					if (a[k][i - 1][j] == 1 && a[k][i][j - 1] == 1)
						a[1 - k][i][j] = 1;
					if (a[k][i - 1][j] == 0 && a[k][i][j - 1] == 0)
						a[1 - k][i][j] = 0;
					if (a[1 - k][i][j] == 1)
						br = false;
				}
			ans++;
			if (br)
				break;
		}
		printf("%d\n", ans);
	}
	return 0;
}
