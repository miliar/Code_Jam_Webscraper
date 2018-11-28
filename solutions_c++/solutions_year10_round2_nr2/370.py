#define  _CRT_SECURE_NO_WARNINGS

#include <vector>
#include <string>
#include <set>
#include <sstream>
#include <map>

#define sz(x) (int)((x).size())
#define all(x) (x).begin(), (x).end()
#define contains(x, y) ((x).find(y) != (x).end())

using namespace std;

typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<vi> vvi;

#define TASK "B-large"

int main()
{
	freopen(TASK ".in", "r", stdin);
	freopen(TASK ".out", "w", stdout);
	int testCount;
	scanf("%d", &testCount);
	for (int c = 1; c <= testCount; c++)
	{
		int n, k, b, t;
		scanf("%d%d%d%d", &n, &k, &b, &t);
		vi x(n), v(n);
		for (int i = 0; i < n; i++)
			scanf("%d", &x[i]);
		for (int i = 0; i < n; i++)
			scanf("%d", &v[i]);
		int got = 0;
		int cur = n - 1;
		int swaps = 0;
		int missed = 0;
		for (; got < k && cur >= 0; cur--)
		{
			int dist = b - x[cur];
			if ((dist - 1) / v[cur] > t - 1)
			{
				missed++;
				continue;
			}
			got++;
			swaps += missed;
		}
		if (got < k)
			printf("Case #%d: IMPOSSIBLE\n", c);
		else printf("Case #%d: %d\n", c, swaps);
	}
	return 0;
}