#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

vector <int> a;
int c[1000];

int main()
{
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		int ml, k, t;
		scanf("%d%d%d", &ml, &k, &t);
		if (k * ml < t)
		{
			printf("Case #%d: IMPOSSIBLE\n", i + 1);
		}
		else
		{
			a.clear();
			memset(c, 0, sizeof(c));
			for (int j = 0; j < t; j++)
			{
				int y;
				scanf("%d", &y);
				a.push_back(y);
			}
			sort(a.begin(), a.end());
			int ans = 0;
			for (int j = t - 1; j >= 0; j--)
			{
				int id = -1;
				int mn = 10000;
				for (int y = 0; y < k; y++)
					if (c[y] < ml && c[y] < mn)
					{
						mn = c[y];
						id = y;
					}
				c[id]++;
				ans += c[id] * a[j];
			}
			printf("Case #%d: %d\n", i + 1, ans);
		}
	}
	return 0;
}
