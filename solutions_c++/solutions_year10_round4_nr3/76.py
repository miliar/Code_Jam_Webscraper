#include <cstdio>
#include <vector>
#include <string>

using namespace std;

int a[102][102];

int main()
{
	int T;
	scanf("%d", &T);
	for (int qn = 1; qn <= T; ++qn)
	{
		memset(a, 0, sizeof(a));
		int n;
		int x1, y1, x2, y2;
		scanf("%d", &n);
		int ret = 0, remain = 0;
		for (int i = 0; i < n; ++i)
		{
			scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
			x1--; y1--; x2--; y2--;
			for (int x = x1; x <= x2; ++x)
				for (int y = y1; y <= y2; ++y)
				{
					if (a[x][y] == 0) remain++;
					a[x][y] = 1;
				}
		}

		while (remain)
		{
			for (int i = 100; i >= 0; --i)
				for (int j = 100; j >= 0; --j)
				{
					int up, left;
					up = (i == 0) ? 0 : a[i - 1][j];
					left = (j == 0) ? 0 : a[i][j - 1];
					if (a[i][j] == 0 && up && left)
					{
						remain++;
						a[i][j] = 1;
					}
					else if (a[i][j] == 1 && (up == 0 && left == 0))
					{
						remain--;
						a[i][j] = 0;
					}
				}
			ret++;
		}
		printf("Case #%d: %d\n", qn, ret);
	}	
}
