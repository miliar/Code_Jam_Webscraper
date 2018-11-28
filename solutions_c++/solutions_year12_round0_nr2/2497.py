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

int n, s, p;
int t;

bool solve()
{
	int ans = 0;

	scanf("%d%d%d", &n, &s, &p);
	for (int i = 0; i < n; i++)
	{
		scanf("%d", &t);
		int mod = t % 3;
		int x = t / 3;
		if (mod == 0)
		{
			if (x >= p)
				ans++;
			else
			{
				if (x > 0 && s > 0 && x + 1 >= p)
				{
					ans++;
					s--;
				}
			}
		}
		else if (mod == 1)
		{
			if (x + 1 >= p)
				ans++;
		}
		else
		{
			if (x + 1 >= p)
				ans++;
			else
			{
				if (s > 0 && x + 2 >= p)
				{
					ans++;
					s--;
				}
			}
		}
	}

	static int TT = 0;
	printf("Case #%d: %d\n", ++TT, ans);

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