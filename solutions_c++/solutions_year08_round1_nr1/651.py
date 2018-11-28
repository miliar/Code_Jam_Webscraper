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
#define MAX_N 900

long long x[MAX_N];
long long y[MAX_N];
int n;

long long solve()
{
	sort(x, x + n);
	sort(y, y + n);
	long long res = 0;
	for (int i = 0; i < n; i++)
		res += x[i] * y[n - i - 1];
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
		scanf("%d", &n);
		for (int i = 0; i < n; i++)
			scanf("%lld", &x[i]);
		for (int i = 0; i < n; i++)
			scanf("%lld", &y[i]);
		printf("Case #%d: %lld\n", test_count + 1, solve());
	}
	return 0;
}