#include <cstdio>
#include <algorithm>
using namespace std;

int main()
{
	int T, caseT, n, sum, xor;

	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);

	scanf("%d", &T);
	for (caseT=1; caseT<=T; ++caseT)
	{
		scanf("%d", &n);
		sum = 0;
		xor = 0;
		int tmp, min = 1<<31-1;
		while (n--)
		{
			scanf("%d", &tmp);
			if (tmp < min) min = tmp;
			sum += tmp;
			xor ^= tmp;
		}
		if (xor != 0) printf("Case #%d: NO\n", caseT);
		else printf("Case #%d: %d\n", caseT, sum-min);
	}

	return 0;
}