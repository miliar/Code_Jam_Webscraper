#include <cstdio>

using namespace std;

int a[10002];

int main()
{
	int t;
	scanf("%d", &t);
	for (int i=1; i<=t; i++)
	{
		int n, l, h;
		scanf("%d %d %d", &n, &l, &h);
		for (int j=0; j<n; j++) scanf("%d", &a[j]);
		bool b2 = 0;
		for (int j=l; j<=h; j++)
		{
			bool b = 1;
			for (int k=0; k<n; k++) if (j%a[k] != 0 && a[k]%j != 0) b = 0;
			if (b)
			{
				printf("Case #%d: %d\n", i, j);
				b2 = 1;
				break;
			}
		}
		if (b2 == 0) printf("Case #%d: NO\n", i);
	}
	return 0;
}
