#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

int main()
{
	freopen("input","r",stdin);
	freopen("output","w",stdout);
	int tt;
	scanf("%d", &tt);
	for (int t = 0; t < tt; ++t)
	{
		int n;
		scanf("%d", &n);
		int s = 0, sx = 0, m = (1 << 30);
		for (int i = 0; i < n; ++i)
		{
			int t;
			scanf("%d", &t);
			sx ^= t;
			s += t;
			m = min(m, t);
		}
		if (sx)
			printf("Case #%d: NO\n", t + 1);
		else
			printf("Case #%d: %d\n", t + 1, s - m);
	}
	return 0;
}
