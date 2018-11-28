#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

bool a[110][110], b[110][110];
int main()
{
	freopen("input", "r", stdin);
	freopen("output", "w", stdout);
	int T, nt, r, x1, y1, x2, y2, i, j, k;
	cin >> T;
	for (nt = 1; nt <= T; nt++)
	{
		cin >> r;
		memset(a, 0, sizeof(a));
		for (i = 1; i <= r; i++)
		{
			cin >> y1 >> x1 >> y2 >> x2;
			for (j = x1; j <= x2; j++)
				for (k = y1; k <= y2; k++)
					a[j][k] = 1;
		}
		for (r = 1; r <= 250; r++)
		{
			for (i = 1; i <= 100; i++)
			{
				for (j = 1; j <= 100; j++)
				{
					if (a[i][j])
						break;
				}
				if (j <= 100)
					break;
			}
		/*	for (i = 1; i <= 5; i++)
			{
				for (j = 1; j <= 5; j++)
					if (a[i][j])
						cout << 1;
					else
						cout << 0;
				cout << '\n';
			}
			putchar('\n');*/
			if (i > 100)
			{
				printf("Case #%d: %d\n", nt, r-1);
				break;
			}
			memcpy(b, a, sizeof(a));
			for (i = 1; i <= 100; i++)
				for (j = 1; j <= 100; j++)
				{
					if (a[i-1][j] && a[i][j-1])
						b[i][j] = 1;
					if (!a[i-1][j] && !a[i][j-1])
						b[i][j] = 0;
				}
			memcpy(a, b, sizeof(b));
		}
	}
	return 0;
}
