#pragma comment(linker, "/STACK:64000000")
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <cassert>
#include <cmath>

using namespace std;

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define forv(i, v) forn(i, v.size())
#define for1(i, n) for (int i = 1; i <= int(n); i++)

#define all(x) x.begin(), x.end()
#define pb push_back
#define mp make_pair

typedef pair<int, int> pii;
typedef vector<int> VI;
typedef long long ll;

int n, m, a;

void solve(int test)
{
	scanf("%d %d %d", &n, &m, &a);

/*	forn(x1, n + 1)
	{
		forn(y2, m + 1)
		{
			forn(x2, n + 1)
			{
				forn(y1, m + 1)
				{
					if (abs(y2 * x1 - x2 * y1) == a)
					{						
						printf("Case #%d: 0 0 %d %d %d %d\n", test, x1, y1, x2, y2);
						return;
					}
				}
			}				
		}
	}
*/
	int x2 = 0, y1 = 0;
	for1(x1, n)
	{
		if (a % x1 == 0 && a / x1 <= m)
		{	
			int y2 = a / x1;
			assert(abs(y2 * x1 - x2 * y1) == a);
			assert(x1 >= 0 && x1 <= n);
			assert(x2 >= 0 && x2 <= n);
			assert(y1 >= 0 && y1 <= m);
			assert(y2 >= 0 && y2 <= m);

			printf("Case #%d: 0 0 %d %d %d %d\n", test, x1, y1, x2, y2);
			return;
		}		
	}

	x2 = 1;

	for1(y2, m)
	{
		int x1 = (a + y2 - 1) / y2;
		if (x1 > n) continue;
		y1 = x1 * y2 - a;
		if (y1 < 0 || y1 > m) continue;
			assert(x1 >= 0 && x1 <= n);
			assert(abs(y2 * x1 - x2 * y1) == a);
			assert(x2 >= 0 && x2 <= n);
			assert(y1 >= 0 && y1 <= m);
			assert(y2 >= 0 && y2 <= m);
		printf("Case #%d: 0 0 %d %d %d %d\n", test, x1, y1, x2, y2);
		return;
	}

	printf("Case #%d: IMPOSSIBLE\n", test);
}
int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int tc; scanf("%d\n", &tc);
	forn(it, tc)
	{
		solve(it + 1);
	}

	return 0;
}
