#pragma comment(linker, "/STACK:16777216")

#include <stdio.h>
#include <stdlib.h>
#include <memory.h>
#include <string.h>
#include <math.h>
#include <assert.h>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <algorithm>
using namespace std;

#define FOR(i, n)	for (int i = 0; i < (int) (n); i++)
#define RFOR(i, n)	for (int i = (int) (n) - 1; i >= 0; i--)
#define CL(x)		memset(x, 0, sizeof(x))
#define CLX(x, v)	memset(x, v, sizeof(x))
#define ALL(x)		x.begin(), x.end()
#define PB			push_back
#define MP			make_pair

typedef long long LL;
typedef unsigned long long UL;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;

//////////////////////////////////////////////////////////////////////////////

const int N = 1000 + 5;

int r, k, n;
int g[N];
LL cost[N];
int test[N];

void solve()
{
	LL tot = 0;
	FOR(i, n) tot += g[i];
	if (tot <= k)
	{
		printf("%lld\n", (LL) r * tot);
		return;
	}

	CL(test);
	CL(cost);

	LL res = 0;

	int i = 0, p = 0;
	while (r)
	{
		if (test[i]) break;
		test[i] = ++p;

		LL kk = 0;
		while (kk + g[i] <= k)
		{
			kk += g[i];
			i = (i + 1) % n;
		}

		res += kk;
		cost[p] = res;
		r--;
	}

	int first = test[i] - 1, last = p;
	int len = last - first;

	if (r) res += (cost[last] - cost[first]) * (r / len) + cost[first + (r % len)] - cost[first];
	printf("%lld\n", res);
}

int main()
{
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int tt;
	scanf("%d", &tt);

	FOR(i, tt)
	{
		scanf("%d %d %d", &r, &k, &n);
		FOR(j, n) scanf("%d", &g[j]);
		printf("Case #%d: ", i + 1);
		solve();
	}

	return 0;
}
