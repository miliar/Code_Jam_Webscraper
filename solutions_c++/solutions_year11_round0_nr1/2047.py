#include <algorithm>
#include <cstdlib>
#include <cstdio>
using namespace std;
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int test;
	scanf("%d", &test);
	for (int testi = 0; testi < test; ++testi)
	{
		int n;
		scanf("%d", &n);
		int pa = 1;
		int pb = 1;
		int ta = 0;
		int tb = 0;
		while (n--)
		{
			char cmd[8];
			int p;
			scanf("%s%d", cmd, &p);
			if (*cmd - 'B')
			{
				if (ta + abs(p - pa) < tb)
				{
					ta = tb + 1;
				}
				else
				{
					ta += abs(p - pa) + 1;
				}
				pa = p;
			}
			else
			{
				if (tb + abs(p - pb) < ta)
				{
					tb = ta + 1;
				}
				else
				{
					tb += abs(p - pb) + 1;
				}
				pb = p;
			}
		}
		printf("Case #%d: %d\n", testi + 1, max(ta, tb));
	}
	return 0;
}