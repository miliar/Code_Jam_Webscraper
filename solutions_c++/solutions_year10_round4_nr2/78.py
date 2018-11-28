#include <cstring>
#include <cstdio>
#include <algorithm>

using namespace std;

int table[2100][12];
int price[1100];
int a[1100];

int main()
{
	int T;
	int n, p;

	scanf("%d", &T);
	for (int qn = 1; qn <= T; ++qn)
	{
		memset(table, -1, sizeof(table));
		int ret = 1999999999;
		scanf("%d", &n);
		int p = (1 << n);

		for (int i = 0; i < p; ++i)
		{
			scanf("%d", &a[i]);
			if (a[i] > 10) a[i] = 10;
		}
		for (int i = n - 1; i >= 0; --i)
			for (int j = 0; j < (1 << i); ++j)
				scanf("%d", &price[(1 << i) + j]);

		for (int j = 0; j < (1 << (n - 1)); ++j)
		{
			int now = (1 << (n - 1)) + j;
			int v = min(a[j * 2], a[j * 2 + 1]);
			table[now][v] = price[now];
			for (int k = v - 1; k >= 0; --k)
				table[now][k] = 0;
		}

		for (int i = n - 2; i >= 0; --i)
		{
			for (int j = 0; j < (1 << i); ++j)
			{
				int now = (1 << i) + j;
				int pr = price[now];

				for (int k = 10; k >= 0; --k)
				{
					if (table[now * 2][k] == -1 || table[now * 2 + 1][k] == -1) continue;
					table[now][k] = pr + table[now * 2][k] + table[now * 2 + 1][k];
					if (table[now * 2][k + 1] != -1 && table[now * 2 + 1][k + 1] != -1)
					{
						if (table[now][k] > table[now * 2][k + 1] + table[now * 2 + 1][k + 1])
						{
							table[now][k] = table[now * 2][k + 1] + table[now * 2 + 1][k + 1];
						}
					}
				}
			}
		}

		for (int i = 0; i <= 10; ++i)
			if (table[1][i] != -1 && ret > table[1][i]) ret = table[1][i];
		
		printf("Case #%d: %d\n", qn, ret);
	}
}

