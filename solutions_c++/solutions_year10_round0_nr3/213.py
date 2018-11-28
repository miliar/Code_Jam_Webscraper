#include <stdio.h>
#include <memory.h>
#include <iostream>
using namespace std;
int flag[1010], num[1010];
long long ans[1010];
int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	int T, tcnt = 1, i;
	long long  r, k, n;
	scanf("%d", &T);
	while (T--)
	{
		cin >> r >> k >> n;
		long long tot = 0;
		for (i = 0; i < n; i++)
		{
			scanf("%d", &num[i]);
			tot += num[i];
		}
		printf("Case #%d: ", tcnt);
		tcnt++;
		if (tot <= k)
			cout << tot * r << endl;
		else
		{
			memset(flag, 0xff, sizeof(flag));
			
			i = 0;
			int cnt = 0;
			long long adjust = 0;
			while (1)
			{
				tot = 0;
				//printf("%d\n", i);
				if (flag[i] != -1)
					break;
				flag[i] = cnt;
				while (1)
				{
					if (tot + num[i] > k)
						break;
					tot += num[i];
					i = (i + 1) % n;
				}
				if (cnt > 0)
					ans[cnt] = ans[cnt - 1] + tot;
				else
					ans[cnt] = tot;
				//printf("%d %d\n", cnt, ans[cnt]);
				cnt++;
				if (cnt == r)
					break;
			}
			//for (int j = 0; j < n; j++)
			//	printf("%d ", flag[j]);
			//printf("\n");
			//printf("%d\n", ans[cnt - 1]);
			if (cnt == r)
				cout << ans[cnt - 1] << endl;
			else
			{
				int b = flag[i] - 1;
				//printf("%d\n", ans[5]);
				cout << (r - b - 1) / (cnt - b - 1) * (ans[cnt - 1] - ans[b])
					+ ans[(r - b - 1) % (cnt - b - 1) + b] << endl;
			}
		}
	}
	return 0;
}
