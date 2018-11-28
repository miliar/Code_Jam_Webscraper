#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <algorithm>

using namespace std;

#define pb push_back
#define sz(a) (int)((a).size())
#define ll long long
#define sqr(a) ((a) * (a))

int n, m, a;
int x1, x2, x3, y1, y2, y3;

void citire()
{
	scanf("%d %d %d\n", &n, &m, &a);
}

void solve()
{
	int ok = 0;

    if (n * m < a)
	{
		printf("IMPOSSIBLE\n");
		return;
	}

	x1 = y1 = 0;
	if (n < m)
	{
		swap(n, m);
		ok = 1;
	}

	x2 = n;
	y3 = a / n;
	if (x2 * y3 < a) ++y3;

	y2 = 1;
	x3 = (x2 * y3 - a);

	if (ok)
	{
		swap(x1, y1);
		swap(x2, y2);
		swap(x3, y3);
	}

	printf("%d %d %d %d %d %d\n", x1, y1, x2, y2, x3, y3);
}

int main()
{
	freopen("date.in", "r", stdin);
	freopen("date.out", "w", stdout);

	int t;

	scanf("%d\n", &t);
	for (int i = 1; i <= t; ++i)
	{
		citire();
		printf("Case #%d: ", i);
		solve();
	}

	return 0;
}
