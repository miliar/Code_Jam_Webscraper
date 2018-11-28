#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <algorithm>
#include <numeric>

using namespace std;

// Spinning Blade

int main()
{
	int cases;
	cin >> cases;

	for (int caseno = 1; caseno <= cases; caseno++) {
		int R, C, D;
		cin >> R >> C >> D;
		vector <string> w(R);
		for (int i = 0; i < R; i++) {
			cin >> w[i];
		}
		vector <vector <vector <int> > > wx(min(R, C) + 1);
		vector <vector <vector <int> > > wy(min(R, C) + 1);
		for (int k = 0; k <= min(R, C); k++) {
			wx[k] = vector <vector <int> >(R + 1, vector <int>(C + 1, 0));
			wy[k] = vector <vector <int> >(R + 1, vector <int>(C + 1, 0));
			if (k > 0) {
				for (int y = 0; y < R; y++) {
					for (int x = 0; x < C; x++) {
						wy[k][y][x] = (w[y][x] - '0') + wy[k - 1][y][x + 1];
						wx[k][y][x] = (w[y][x] - '0') + wx[k - 1][y + 1][x];
					}
				}
			}
		}
		int ret = 0;
		for (int k = min(R, C); k >= 3; k--) {
			for (int y = 0; y <= R - k; y++) {
				for (int x = 0; x <= C - k; x++) {
					int xsum = 0;
					for (int xx = 0; xx < k; xx++) {
						if (xx == 0 || xx == k - 1) {
							xsum += wx[k - 2][y + 1][x + xx] * (xx * 2 - k + 1);
						} else {
							xsum += wx[k][y][x + xx] * (xx * 2 - k + 1);
						}
					}
					int ysum = 0;
					for (int yy = 0; yy < k; yy++) {
						if (yy == 0 || yy == k - 1) {
							ysum += wy[k - 2][y + yy][x + 1] * (yy * 2 - k + 1);
						} else {
							ysum += wy[k][y + yy][x] * (yy * 2 - k + 1);
						}
					}
					if (xsum == 0 && ysum == 0) {
						ret = k;
					}
					if (ret > 0) break;
				}
				if (ret > 0) break;
			}
			if (ret > 0) break;
		}
		cout << "Case #" << caseno << ": ";
		if (ret == 0) {
			cout << "IMPOSSIBLE" << endl;
		} else {
			cout << ret << endl;
		}
	}

	return 0;
}
