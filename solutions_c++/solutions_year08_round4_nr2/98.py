#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <map>
#include <algorithm>
#include <stdio.h>
#include <string>
#include <vector>
#include <queue>
#include <cassert>
#include <cmath>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
const int INF = 1000000000;

typedef pair<int, int> pii;

#define all(s) s.begin(), s.end()

int triangle_square_2 (int x1, int y1, int x2, int y2, int x3, int y3)
{
	return
		(x1 * y2 - x1 * y3) +
		(x2 * y3 - x2 * y1) +
		(x3 * y1 - x3 * y2);
}


int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; ++test)
	{
		cerr << test << endl;
		int n, m, a;
		cin >> n >> m >> a;
		bool found = false;
		for (int x2 = 0; x2 <= n && !found; ++x2)
			for (int y2 = 0; y2 <= m && !found; ++y2)
				for (int x3 = 0; x3 <= n && !found; ++x3)
					for (int y3 = 0; y3 <= m && !found; ++y3)
					{
						if (abs(triangle_square_2(0, 0, x2, y2, x3, y3)) == a)
						{
							printf("Case #%d: %d %d %d %d %d %d\n", test, 0, 0, x2, y2, x3, y3);
							found = true;
						}
					}

		if (!found)
			printf("Case #%d: IMPOSSIBLE\n", test);
	}

}