#include <cstdio>

using namespace std;

int main()
{
	int n;
	scanf("%d", &n);
	for (int i=1; i<=n; i++)
	{
		int m;
		scanf("%d", &m);
		int x = 0, sum = 0, min = 9999999;
		for (int j=0; j<m; j++)
		{
			int t;
			scanf("%d", &t);
			x = x^t;
			sum += t;
			if (t < min) min = t;
		}
		printf("Case #%d: ", i);
		if (x == 0) printf("%d\n", sum-min);
		else printf("NO\n");
	}
	return 0;
}
