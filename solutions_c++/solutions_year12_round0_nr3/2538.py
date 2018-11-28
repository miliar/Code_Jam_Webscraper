#include <stdio.h>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <memory.h>
#include <algorithm>
#include <cassert>
#include <math.h>

using namespace std;

#define mp make_pair
#define pb push_back
#define _(a, b) memset(a, b, sizeof(a))

typedef long long lint;
typedef unsigned long long ull;

const double eps = 1e-9;
const int INF = 1000000000;
const lint LINF = 4000000000000000000ll;

void prepare()
{
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
#else
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
}

set<int> val;
bool solve()
{
	int a, b;
	scanf("%d%d", &a, &b);

	int l = 0, x = a, mul = 1;
	while (x)
	{
		x /= 10;
		l++;
		mul *= 10;
	}

	mul /= 10;

	lint ans = 0;
	for (int i = a; i <= b; i++)
	{
		val.clear();
		
		x = i;
		for (int j = 1; j < l; j++)
		{
			x = (x % 10) * mul + (x / 10);
			if (x >= a && x < i)
				val.insert(x);
		}

		ans += val.size();
	}

	static int TT = 0;
	printf("Case #%d: %lld\n", ++TT, ans);

	return false;
}

int main()
{
	prepare();
	int tn;
	for (scanf("%d", &tn); tn; tn--)
		solve();
	return 0;
}