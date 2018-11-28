#include <stdio.h>
#include <iostream>
using namespace std;
int flag[1010], value[1010];
long long ans[1010];
long long  r, k, n;
int ringp;
int main()
{
	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);
	int tcase, flagcase = 1, i;
	scanf("%d", &tcase);
	while (tcase--)
	{
		cin >> r >> k >> n;
		long long total = 0;
		for (i = 0; i < n; i++)
		{
			scanf("%d", &value[i]);
			total += value[i];
		}
		printf("Case #%d: ", flagcase++);
		if (total <= k)
		{
			cout << total * r << endl;
			continue;
		}
		memset(flag, -1, sizeof(flag));
		i = 0;
		ringp = 0;
		while(1)
		{
			total = 0;
			if (flag[i] != -1)break;
			flag[i] = ringp;
			while(1)
			{
				if (total + value[i] > k)break;
				total += value[i];
				i = (i + 1) % n;
			}
			if (ringp > 0)
			{
				ans[ringp] = ans[ringp - 1] + total;
			}
			else{
				ans[ringp] = total;
			}
			ringp++;
			if (ringp == r)break;
		}
		if (ringp == r){
			cout << ans[ringp - 1] << endl;
		}
		else
		{
			int p = flag[i] - 1;
			cout << (r - p - 1)/(ringp - p - 1)*(ans[ringp - 1] - ans[p])
				+ ans[(r -p - 1)%(ringp - p - 1) + p] << endl;
		}
	}
	return 0;
}
