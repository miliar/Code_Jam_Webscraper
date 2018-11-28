#include <stdio.h>
#include <math.h>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <deque>
#include <string>
#include <cassert>
#include <iostream>
#include <memory.h>
#include <algorithm>

using namespace std;

#define mp make_pair
#define pb push_back
#define _(a, b) memset(a, b, sizeof(a))

typedef long long lint;
typedef unsigned long long ull;

const int INF = 1000000000;
const lint LINF = 1000000000000000000LL;

void prepare()
{
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
#else
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
}

int n, p;
int d[10005], l[10005], w[10005];

bool solve()
{
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
		scanf("%d%d", &d[i], &l[i]);

	scanf("%d", &p);

	for (int i = 0; i < 10005; i++)
		w[i] = -1;

	bool ans = false;

	w[0] = 2 * d[0];
	for (int i = 0; i <= n; i++)
		if (w[i] >= 0)
		{
			if (w[i] >= p)
			{
				ans = true;
				break;
			}

			for (int j = i + 1; j < n; j++)
			{
				if (d[j] > w[i])
					break;

				int r1 = d[j] + min(d[j] - d[i], l[j]);
				w[j] = max(w[j], r1);
			}
		}

	static int TT = 0;
	printf("Case #%d: ", ++TT);
	if (ans)
		printf("YES\n");
	else
		printf("NO\n");

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