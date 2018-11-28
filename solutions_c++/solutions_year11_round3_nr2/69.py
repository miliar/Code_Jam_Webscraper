#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <cctype>

using namespace std;
template <class T> T sqr(T a) { return a * a; }
#define maxn 1001000

long long a[maxn];
int l, n;
long long t;

long long solve()
{
	long long sum = 0;
	long long num = -1, denom;
	for (int i = 0; i < n; i++)
	{
		sum += a[i] * 4;
		if (sum < t)
			a[i] = 0;
		else if (sum - a[i] * 4 < t * 2)	
			a[i] = sum / 2 - t;
		else
			a[i] *= 2;
	}
	sort(a, a + n);
	int j;
	for (int i = n - 1, j = 0; i >= 0, j < l; i--, j++)
		sum -= a[i];
	return sum / 2;
}

int main()
{
#ifdef impetus
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int testnum;
	scanf("%d", &testnum);
	for (int tc = 0; tc < testnum; tc++)
	{
		int c;
		scanf("%d%lld%d%d", &l, &t, &n, &c);
		for (int i = 0; i < c; i++)
		{
			int pp;
			scanf("%d", &pp);
			for (int j = i; j < n; j += c)
				a[j] = pp;
		}
		printf("Case #%d: %lld\n", tc + 1, solve());
	}
	return 0;
}