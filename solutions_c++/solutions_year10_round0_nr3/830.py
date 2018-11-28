#include <iostream>

using namespace std;


int g[1100];
long long ans[1100];
int use[1100];


int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int i = 0; i < t; i++)
	{
		memset(use, 0, sizeof(use));
		memset(ans, 0, sizeof(ans));
		int r,k,n;
		scanf("%d%d%d", &r, &k, &n);
		printf("Case #%d: ", i + 1);
		long long s = 0;
		for(int j = 0; j < n; j++)
		{
			scanf("%d", &g[j]);
			s += g[j];
		}
		if(s <= k)
		{
			printf("%lld\n", (long long)r * s);
			continue;
		}
		int current = 0;
		long long res = 0;
		int time = 1;
		for(int x = 0; x < r; x++)
		{
			long long c = 0;
			int next = -1;
			for(int j = current; true; (++j)%=n)
			{
				if(c + g[j] > k)
				{
					next = j;
					break;
				}
				c += g[j];				
			}
			res += (ans[time++] = c);
			use[current] = time - 1;
			if(use[next])
			{
				long long period = 0;
				for(int j = use[next]; j < time; j++)
				{
					period += ans[j];
				}
				int remain = r - x - 1;
				int lengthOfPeriod = time - use[next];
				res += period * (long long)(remain / lengthOfPeriod);
				int lastStep = remain % lengthOfPeriod;
				for(int j = 0; j < lastStep; j++)
				{
					res += ans[j + use[next]];
				}
				break;
			}
			current = next;
		}
		printf("%lld\n", res);
	}
	return 0;
}