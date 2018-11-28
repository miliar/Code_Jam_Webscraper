#include <algorithm>
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
		int minn = 0x7fffffff;
		int sum = 0;
		int res = 0;
		while (n--)
		{
			int a;
			scanf("%d", &a);
			minn = min(minn, a);
			sum += a;
			res ^= a;
		}
		if (res)
		{
			printf("Case #%d: NO\n", testi + 1);
		}
		else
		{
			printf("Case #%d: %d\n", testi + 1, sum - minn);
		}
	}
	return 0;
}