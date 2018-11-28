#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

int n, t;
int r, k;
int g[1000000];

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	scanf("%d", &t);
	for (int tt = 1; tt <= t; tt++)
	{
		scanf("%d%d%d", &r, &k, &n);
		int tot = 0;
		for (int i = 0; i < n; i++)
		{
			scanf("%d", &g[i]);
			tot += g[i];
		}
		k = min(k, tot);
		for (int i = n; i < r * k * n; i++)
			g[i] = g[i % n];
		long long ans = 0;
		int cur = 0;
		for (int i = 0; i < r; i++)
		{
			int sum = 0;
			while (1)
			{
				if (sum + g[cur] > k)
					break;
				sum += g[cur];
				cur++;
			}
			ans += sum;
		}
		printf("Case #%d: ", tt);
		cout << ans << endl;
	}
	return 0;
}
