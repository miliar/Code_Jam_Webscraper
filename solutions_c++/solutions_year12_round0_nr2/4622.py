#include<stdio.h>
#include<algorithm>

using namespace std;

int a[105];

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);

	int tt;

	scanf("%d", &tt);

	for(int t = 1; t <= tt; t++)
	{
		int n, s, p;
		scanf("%d%d%d", &n, &s, &p);

		for(int i = 0; i < n; i++)
			scanf("%d", &a[i]);

		sort(a, a+n);

		int res = 0;

		for(int i = n-1; i >= 0; i--)
		{
			if(a[i] % 3 == 0 && a[i] / 3 >= p ||
				a[i] % 3 == 2 && (a[i]+1) / 3 >= p ||
				a[i] % 3 == 1 && (a[i]+2) / 3 >= p)
				res++;
			else if(a[i] >= 2 && s > 0)
			{
				if(a[i] % 3 == 0 && (a[i] / 3) + 1 >= p || 
					a[i] % 3 == 2 && (a[i] / 3) + 2 >= p)
					res++, s--;
			}
		}

		printf("Case #%d: %d\n", t, res);
	}

	return 0;
}