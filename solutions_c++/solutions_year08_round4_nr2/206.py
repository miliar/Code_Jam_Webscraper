#include <iostream>
#include <cmath>
using namespace std;

int m, n, a;
bool check()
{
	int i, j, ii, jj;
	for (i = 0; i <= n; ++ i)
		for (j = 0; j <= n; ++ j)
			for (ii = 0; ii <= m; ++ ii)
				for (jj = 0; jj <= m; ++ jj)
					if (abs(i * jj - ii * j) == a)
					{
						printf("0 0 %d %d %d %d\n", i, ii, j, jj);
						return true;
					}
	return false;
}

int main()
{
	freopen("B-small-attempt1.in", "r", stdin);
	freopen("B-small-attempt1.out", "w", stdout);
	int T, Case = 1;
	scanf("%d", &T);
	while (T --)
	{
		scanf("%d %d %d", &n, &m, &a);

		printf("Case #%d: ", Case ++);
		if (!check())
			puts("IMPOSSIBLE");
	}
	return 0;
}