#include <iostream>
#include <vector>


using namespace std;


long long a[3000];
long long res[3000];
vector<long long> v;
bool used[3000];


int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int tests;
	scanf("%d", &tests);
	for(int asdf = 0; asdf < tests; asdf++)
	{
		memset(used, false, sizeof(used));
		long long r, k, n;
		v.clear();
		scanf("%lld%lld%lld", &r, &k, &n);
		printf("Case #%d: ", asdf + 1);
		for(int i = 0; i < n; i++)
			scanf("%lld", &a[i]);
		long long sum = 0;
		for(int i = 0; i < n; i++)
			sum += a[i];
		if(sum <= k)
		{
			printf("%lld\n", r * sum);
			continue;
		}
		for(int i = 0; i < n; i++)
			a[n + i] = a[i];
		long long now = 0;
		int m = 1;
		res[0] = 0;
		do
		{
			used[now] = true;
			v.push_back(now);
			long long cur = 0;
			while(cur + a[now] <= k)
			{
				cur += a[now];
				now++;
			}
			now %= n;
			res[m] = res[m - 1] + cur;
			m++;
		}while(!used[now] && m - 1 < r);
		long long ans = 0;
		if(m - 1 == r)
		{
			ans = res[m - 1];
		}
		else
		{
			m--;
			long long x = 0;
			while(v[x] != now)
			{
				x++;
				r--;
			}
			ans = res[x] + (r / (m - x)) * (res[m] - res[x]) + (res[x + r % (m - x)] - res[x]);
		}
		printf("%lld\n", ans);
	}
}