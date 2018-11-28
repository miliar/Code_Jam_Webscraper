#include <cstdio>
using namespace std;

long long r, k;
int n;
long long g[1010];
long long count[1010];
long long loopsum[1010];
int id[1010];
int main()
{
	int t;
	int i, j, h;
	int loop;
	long long sum;
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	scanf("%d", &t);
	for (i = 1; i <= t; i++)
	{
		scanf("%lld%lld%d", &r, &k, &n);
		for (j = 0; j < n; j++)
		{
			scanf("%lld", g + j);
			count[j] = 0;
			loopsum[j] = 0;
		}	
		loopsum[n] = 0;
		j = 0;
		loop = 0;
		while (!count[j])
		{
			h = j;
			while (count[j] + g[h] <= k)
			{
				count[j] += g[h];
				h++;
				if (h == n)
					h = 0;
				if (h == j)
					break;
			}
			loop++;
			loopsum[loop] += loopsum[loop - 1] + count[j];
			id[j] = loop;
			j = h;
		}
		if (r < id[j])
			printf("Case #%d: %lld\n", i, loopsum[r]);
		else
		{
			r -= id[j] - 1;
			sum = (r / (loop - id[j] + 1)) * (loopsum[loop] - loopsum[id[j] - 1]) + loopsum[r % (loop - id[j] + 1) + id[j] - 1];
			printf("Case #%d: %lld\n", i, sum);
		}
	}
	return 0;
}