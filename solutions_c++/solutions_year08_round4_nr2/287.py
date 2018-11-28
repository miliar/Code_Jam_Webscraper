#include <cstdio>
#include <cstring>
#include <math.h>
#include <algorithm>
#include <string>
#include <vector>
#include <cctype>
#include <bitset>
#include <sstream>
#include <set>
#include <map>

using namespace std;
template <class T> T sqr(T a) { return a * a; }
#define memfill(a, b) memset(a, b, sizeof(a))
#define pb push_back
#define vi vector<int>
#define vii vector<vector<int> >
#define vs vector<string>
#define pii pair<int, int>
#define dist(a, b) sqrt(sqr(a.x - b.x) + sqr(a.y - b.y))
#define bound(x, y, n, m) x >= 0 && y >= 0 && x < n && y < m
#define maxn 12000

long long n, m, a;

long long aabs(long long d)
{
	if (d < 0)
		return -d;
	return d;
}

int solve()
{
	for (long long i = -n; i <= n; i++) if (i)
		for (long long j = -m; j <= m; j++)
			for (long long k = -n; k <= n; k++)
			{
				long long l = (a + j * k) / i;
				if (aabs(i - k) <= n && aabs(j - l) <= m && aabs(l) <= m && a == i * l - j * k)
				{
					long long x = -min(i, k);
					long long y = -min(j, l);
					printf("%lld %lld %lld %lld %lld %lld\n", x, y, i + x, j + y, k + x, l + y);
					return 1;
				}
			}
		for (long long j = -m; j <= m; j++)
			for (long long k = -n; k <= n; k++)
			{
				long long i = 0;
				long long l = 0;
				if (a == i * l - j * k)
				{
					long long x = -min(i, k);
					long long y = -min(j, l);
					printf("%lld %lld %lld %lld %lld %lld\n", x, y, i + x, j + y, k + x, l + y);
					return 1;
				}
			}
	return 0;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int test_num;
	scanf("%d", &test_num);
	for (int test_count = 0; test_count < test_num; test_count++)
	{
		scanf("%lld%lld%lld", &n, &m, &a);
		printf("Case #%d: ", test_count + 1);
		int fb = solve();
		if (!fb)
			printf("IMPOSSIBLE\n");
	}
	return 0;
}