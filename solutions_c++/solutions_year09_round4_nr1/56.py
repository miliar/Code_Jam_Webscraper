#include <iostream>
using namespace std;

const int N = 100;
int a[N];
char buf[N];

int main()
{
	int cas, num = 0;
	freopen("A-large.in", "r", stdin);
	freopen("A.out", "w", stdout);
	scanf("%d", &cas);
	while (cas--)
	{
		int n;
		int i, j, k;
		scanf("%d", &n);
		for (i = 0; i < n; ++i)
		{
			int m = -1;
			scanf("%s", buf);
			for (j = 0; j < n; ++j)
			{
				if (buf[j] != '0') m = j;
			}
			a[i] = m;
		}
		int ret = 0;
		for (i = 0; i < n; ++i)
		{
			if (a[i] <= i) continue;
			for (j = i + 1; j < n; ++j)
				if (a[j] <= i) break;
			ret += j - i;
			for (k = j; k > i; --k)
				a[k] = a[k - 1];
		}
		printf("Case #%d: %d\n", ++num, ret);
	}
	return 0;
}
