#include <cstdio>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <cstring>
#include <cstdlib>
#include <cmath>

using namespace std;

const int MaxN = 20;
const double eps = 1e-7;

string Map[MaxN];

int R, C, D;

int main()
{
	int Ncase;
	freopen("b_small.in", "r", stdin);
	freopen("b_small.out", "w", stdout);
	cin >> Ncase;
	for (int run = 0; run < Ncase; ++run)
	{
		cin >> R >> C >> D;
		for (int i = 0; i < R; ++i)
			cin >> Map[i];

		int ans = -1;
		for (int i = min(R, C); i >= 3; --i)
		{
			double center = 1.0 * i / 2;
			for (int r = 0; r <= R - i; ++r)
			{
				for (int c = 0; c <= C - i; ++c)
				{
					double sumx = 0, sumy = 0;
					for (int r1 = 0; r1 < i; ++r1)
						for (int c1 = 0; c1 < i; ++c1)
						{
							if (r1 == 0 && c1 == 0 || r1 == i-1 && c1 == 0 ||
								r1 == 0 && c1 == i-1 || r1 == i-1 && c1 == i-1)
							continue;
							sumx += (r1 + 0.5 - center) * Map[r + r1][c + c1];
							sumy += (c1 + 0.5 - center) * Map[r + r1][c + c1];
						}
					//cout << sumx << " " << sumy << endl;
					if (fabs(sumx) < eps && fabs(sumy) < eps)
					{
						ans = i;
						break;
					}
				}
				if (ans != -1) break;
			}
			if (ans != -1) break;
		}
		cout << "Case #" << run+1 << ": ";
		if (ans != -1) cout << ans << endl;
		else cout << "IMPOSSIBLE" << endl;
	}
}
