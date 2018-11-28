#include <stdio.h>
#include <vector>

using namespace std;

int t, n, r;
long long k;
vector<long long> groups;
vector< pair<int, long long> > rez;
long long sum;
int cur = 0;

int main()
{
	freopen("B-small.in", "r", stdin);
	freopen("B-small.out", "w", stdout);
	scanf("%d", &t);

	for (int i = 0; i < t; i++)
	{
		scanf("%d%lld%d", &r, &k, &n);
		
		groups.resize(n);
		rez.resize(n);

		for (int j = 0; j < n; j++)
			scanf("%lld", &groups[j]);

		for (int j = 0; j < n; j++)
		{
			sum = 0;

			for (int u = 0; u < n; u++)
			{
				if (sum + groups[(j + u) % n] > k)
				{
					rez[j] = make_pair((j + u) % n, sum);
					break;
				}
				else
					sum += groups[(j + u) % n];

				if (u == n - 1)
					rez[j] = make_pair((j + u) % n, sum);
			}
		}

		sum = 0;
		cur = 0;

		for (int j = 0; j < r; j++)
		{
			sum += rez[cur].second;
			cur = rez[cur].first;
		}

		printf("Case #%d: %lld\n", i + 1, sum); 
	}
	return 0;
}