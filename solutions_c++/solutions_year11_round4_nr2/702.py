#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <string>
#include <cstring>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <ctime>
#include <cassert>
#include <functional>
#include <iterator>
#include <utility>

typedef long double LD;
typedef long long LL;
typedef unsigned long long ULL;
using namespace std;

const int N_MAX = 550;
int a[N_MAX][N_MAX];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tests;
	cin >> tests;
	for (int nt = 1; nt <= tests; ++nt)
	{
		cerr << "-- Test " << nt << " --\n";

		int r, c, d;
		cin >> r >> c >> d;
		for (int i = 0; i < r; ++i) for (int j = 0; j < c; ++j)
		{
			char w;
			cin >> w;
			a[i][j] = d + (int)(w - '0');
		}
		int ans = 0;

		for (int k = 3; k <= min(r, c); ++k)
		{
			LL dx = 0, dy = 0;
			int cx, cy;

			for (int ii = 0; ii + k <= r; ++ii) for (int jj = 0; jj + k <= c; ++jj)
			{
				cy = k + 2 * jj;
				cx = k + 2 * ii;

				dx = dy = 0;
				for (int i = 0; i < k; ++i)
					for (int j = 0; j < k; ++j)
					{	
						if ((i == 0 && j == 0) || (i == 0 && j == k - 1) || (i == k - 1 && j == 0) || (i == k - 1 && j == k - 1)) continue;
						dx += (LL)(1 + 2 * (i + ii) - cx) * a[i + ii][j + jj];
						dy += (LL)(1 + 2 * (j + jj) - cy) * a[i + ii][j + jj];
					}
				if (dx == 0 && dy == 0) ans = k;
			}
		}
		cout << "Case #" << nt << ": ";
		if (ans > 0) cout << ans << '\n'; else cout << "IMPOSSIBLE\n";
		
	}
	return 0;
}
