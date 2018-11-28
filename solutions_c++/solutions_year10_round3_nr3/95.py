#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

int m, n, t;
int p[40][40];
int ans[60];

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	scanf("%d", &t);
	for (int tt = 1; tt <= t; tt++)
	{
		printf("Case #%d: ", tt);
		memset(ans, 0, sizeof(ans));
		scanf("%d%d\n", &n, &m);
		memset(p, 0, sizeof(p));
		char c;
		for (int i = 0; i < n; i++, scanf("\n"))
			for (int j = 0; j < m / 4; j++)
			{
				scanf("%c", &c);
				int temp;
				if (c <= '9')
					temp = c - '0';
				else
					temp = c - 'A' + 10;
				if (temp & 8)
					p[i][j * 4] = 1;
				if (temp & 4)
					p[i][j * 4 + 1] = 1;
				if (temp & 2)
					p[i][j * 4 + 2] = 1;
				if (temp & 1)
					p[i][j * 4 + 3] = 1;
			}		
//		for (int i = 0; i < n; i++, printf("\n"))
//			for (int j = 0; j < m; j++)
//				printf("%d", p[i][j]);
//		printf("\n");
		for (int len = min(n, m); len >= 1; len--)
			for (int i = 0; i + len <= n; i++)
				for (int j = 0; j + len <= m; j++)
				{
					int c = p[i][j];
					if (c > 1)
						continue;
					bool bb = true;
					for (int ii = 0; ii < len && bb; ii++)
						for (int jj = 0; jj < len && bb; jj++)
						{
							if ((ii + jj) % 2 == 0 && p[i + ii][j + jj] != c)
								bb = false;
							if ((ii + jj) % 2 == 1 && p[i + ii][j + jj] != 1 - c)
								bb = false;
						}
					if (bb)
					{
						ans[len]++;
						for (int ii = 0; ii < len; ii++)
							for (int jj = 0; jj < len; jj++)
								p[i + ii][j + jj] = 2;
//						for (int ii = 0; ii < n; ii++, printf("\n"))
//							for (int jj = 0; jj < m; jj++)
//								printf("%d", p[ii][jj]);
//						printf("\n");
					}
				}
		int kol = 0;
		for (int i = 0; i <= min(n, m); i++)
			if (ans[i] > 0)
				kol++;
		printf("%d\n", kol);
		for (int i = min(n, m); i >= 1; i--)
			if (ans[i] > 0)
				printf("%d %d\n", i, ans[i]);
	}
	return 0;
}
