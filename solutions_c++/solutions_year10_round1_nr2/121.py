#include <cstdio>
#include <cstring>

#define abs(x) (((x) > 0) ? (x) : -(x))

using namespace std;

int a[105];
int table[102][257];

int main()
{
	int T;
	scanf("%d", &T);
	int D, I, M, n;

	for (int qn = 1; qn <= T; ++qn)
	{
		scanf("%d %d %d %d", &D, &I, &M, &n);
		for (int i = 0; i < n; ++i)
			scanf("%d", &a[i]);
		for (int i = 0; i <= 255; ++i)
			table[0][i] = abs(a[0] - i);
		for (int i = 1; i < n; ++i)
		{
			for (int j = 0; j <= 255; ++j)
			{
				// D
				table[i][j] = table[i - 1][j] + D;
				
				// C & I
				for (int k = 0; k <= 255; ++k)
				{
					// j 로 바꾸고, i를 하는거.
					int tmp = table[i - 1][k] + abs(a[i] - j);
					int diff = abs(k - j);
					if (diff > M) 
					{
						if (M == 0) tmp = 999999999; else tmp += (diff - 1) / M * I;
					}
					if (table[i][j] > tmp) table[i][j] = tmp;
				}
			}
		}

		int ret = table[n - 1][0];
		for (int i = 1; i <= 255; ++i)
			if (ret > table[n - 1][i]) ret = table[n - 1][i];
		printf("Case #%d: %d\n", qn, ret);
	}
}

