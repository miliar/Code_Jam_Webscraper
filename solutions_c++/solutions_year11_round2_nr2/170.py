#include <algorithm>
#include <cstdio>
#include <vector>
using namespace std;

#define maxn 222

int n,d;
int p[maxn], v[maxn];

bool ok(long long mid)
{
	long long next = -1000000000000000LL;
	for(int i = 0; i < n; i++)
	{
		long long low = max(next, p[i] - mid);
		long long high = low + 1LL * (v[i]-1) * d;
		if(high - p[i] > mid) return 0;
		next = high+d;
	}
	return 1;
}

void test()
{
	scanf("%d%d", &n, &d);
	d *= 2;
	for(int i = 0; i < n; i++)
	{
		scanf("%d%d", &p[i], &v[i]);
		p[i] *= 2;
	}
	long long low = -1, high = 1000000000000000LL;
	while(low+1 < high)
	{
		long long mid = (low+high) / 2;
		if(ok(mid)) high = mid;
		else low = mid;
	}
	printf("%lld.%lld\n", high/2, 5*(high%2));
}

int main()
{
	int tt;
	scanf("%d", &tt);
	for(int i = 1; i <= tt; i++)
	{
		printf("Case #%d: ", i);
		test();
	}
}
