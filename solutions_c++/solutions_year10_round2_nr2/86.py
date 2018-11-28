#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <vector>

using namespace std;

const long double EPS = 1e-9;
const long double PI = 3.1415926535897932384626433832795;

typedef long double ld;
typedef long long i64;
typedef pair <int, int> PII;

int n, k, b, t;
int x[64];
int v[64];

int main()
{
	freopen("B-large.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int tcn;
	scanf("%d", &tcn);
	for (int tc = 1; tc <= tcn; tc++)
	{
		scanf("%d%d%d%d", &n, &k, &b, &t);
		for (int i = 0; i < n; i++)
			scanf("%d", &x[i]);
		for (int i = 0; i < n; i++)
			scanf("%d", &v[i]);

		int ans = 0, z = 0;
		for (int i = n - 1; i >= 0; i--)
		{
			if (b - x[i] <= t * v[i])
			{
				if (k)
				{
					ans += z;
					k--;
				}
			}
			else z++;
		}

		printf("Case #%d: ", tc);
		if (k) printf("IMPOSSIBLE\n");
		else printf("%d\n", ans);
	}

	return 0;
}
