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
#define maxn 1200

int p, k, n;
long long f[maxn];

long long solve()
{
	sort(f, f + n);
	long long res = 0;
	int e = 0;
	int d = 1;
	for (int i = n - 1; i >= 0; i--)
	{
		if (e == k)
		{
			d++;
			e = 0;
		}
		if (d > p && f[i] > 0)
			return -1;
		res += f[i] * d;
		e++;
	}	
	return res;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int test_num;
	scanf("%d", &test_num);
	for (int test_count = 0; test_count < test_num; test_count++)
	{
		scanf("%d%d%d", &p, &k, &n);
		for (int i = 0; i < n; i++)
			scanf("%lld", &f[i]);
		int t = solve();
		if (t + 1)
			printf("Case #%d: %lld\n", test_count + 1, solve());
		else
			printf("Case #%d: Impossible\n", test_count + 1);
	}
	return 0;
}