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
#define mod 1000000007

long long a[maxn];
int n;

long long add(long long a, long long b)
{
	return (a + b) % mod;
}

long long mult(long long a, long long b)
{
	return (a * b) % mod;
}

long long solve()
{
	long long p[maxn];
	long long res = 0;
	for (int i = 0; i < n; i++)
	{
		p[i] = 1;
		for (int j = 0; j < i; j++)
			if (a[j] < a[i])
				p[i] = add(p[i], p[j]);
		res = add(res, p[i]);
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
		int m;
		long long x, y, z;
		long long aux[800];
		scanf("%d%d%lld%lld%lld", &n, &m, &x, &y, &z);
		for (int i = 0; i < m; i++)
			scanf("%lld", &aux[i]);
		for (int i = 0; i < n; i++)
		{
			a[i] = aux[i % m];
			aux[i % m] = (aux[i % m] * x + (i + 1) * y) % z;
		}
		printf("Case #%d: %lld\n", test_count + 1, solve());
	}
	return 0;
}