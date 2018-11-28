#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

int n, t;
int beg[1100], end[1100];

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	scanf("%d", &t);
	for (int tt = 1; tt <= t; tt++)
	{
		printf("Case #%d: ", tt);
		scanf("%d", &n);
		int ca, cb;
		for (int i = 0; i < n; i++)
		{
			scanf("%d%d", &ca, &cb);
			beg[i] = ca;
			end[i] = cb;
		}
		int ans = 0;
		for (int i = 0; i < n; i++)
			for (int j = 0; j < i; j++)
			{
				if (beg[j] > beg[i] && end[j] < end[i])
					ans++;
				if (beg[j] < beg[i] && end[j] > end[i])
					ans++;
			}
		printf("%d\n", ans);
	}
	return 0;
}
