#include <cstdio>
#include <cstdlib>
#include <cstring>
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

// Perpetual Motion

int main()
{
	int cases;
	cin >> cases;

	for (int caseno = 1; caseno <= cases; caseno++) {
		int R, C;
		cin >> R >> C;
		vector <string> conv(R);
		for (int i = 0; i < R; i++) {
			cin >> conv[i];
		}
		string dir = "|\\-/";
		int dx[4] = { 0, 1, 1,-1};
		int dy[4] = { 1, 1, 0, 1};
		int ret = 0;
		for (int b = 0; b < 1 << (R * C); b++) {
			bool ok = true;
			vector <bool> oc(R * C, false);
			for (int y = 0; y < R; y++) {
				for (int x = 0; x < C; x++) {
					int p = y * C + x;
					int d = dir.find(conv[y][x]);
					int sign = (b & (1 << p)) ? 1 : -1;
					int nx = x + sign * dx[d];
					int ny = y + sign * dy[d];
					nx = (nx + C) % C;
					ny = (ny + R) % R;
					if (oc[ny * C + nx]) {
						ok = false;
					}
					oc[ny * C + nx] = true;
				}
			}
			if (ok) {
				ret++;
			}
		}

		cout << "Case #" << caseno << ": " << ret << endl;
	}

	return 0;
}
