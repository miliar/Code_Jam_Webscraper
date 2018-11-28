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
#define maxn 800

long long n, a, b, c, d, m;

long long x[maxn];
long long y[maxn];

int solve()
{
	for (int i = 1; i < n; i++)
	{
		x[i] = (a * x[i - 1] + b) % m;
		y[i] = (c * y[i - 1] + d) % m;
	}
	int res = 0;
	for (int i = 0; i < n; i++)
		for (int j = i + 1; j < n; j++)
			for (int k = j + 1; k < n; k++)
				if ((x[i] + x[j] + x[k]) % 3 == 0 && (y[i] + y[j] + y[k]) % 3 == 0/* &&
					(x[i] - x[k]) * (y[j] - y[k]) - (x[j] - x[k]) * (y[i] - y[k]) != 0*/)
					res++;
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
		scanf("%d%lld%lld%lld%lld%lld%lld%lld", &n, &a, &b, &c, &d, &x[0], &y[0], &m);
		printf("Case #%d: %d\n", test_count + 1, solve());
	}	
	return 0;
}