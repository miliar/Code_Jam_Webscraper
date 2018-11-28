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

// Aerobics
int main()
{
	int cases;
	cin >> cases;

	for (int caseno = 1; caseno <= cases; caseno++) {
		int N, W, L;
		cin >> N >> W >> L;
		vector <pair <int, int> > r(N);
		for (int i = 0; i < N; i++) {
			cin >> r[i].first;
			r[i].second = i;
		}
		int w = min(W, L);
		int h = max(W, L);
		sort(r.begin(), r.end());
		vector <int> rx(N);
		vector <int> ry(N);
		int nx = r.size();
		int ny = r.size();
		int dir = 1;
		for (int i = r.size() - 1; i >= 0; i--) {
			int x;
			if (dir == 1) {
				x = 0;
				for (int j = nx; j < ny; j++) {
					x = max(x, r[j].first + rx[j] + r[i].first);
				}
			} else {
				x = w;
				for (int j = nx; j < ny; j++) {
					x = min(x, -r[j].first + rx[j] - r[i].first);
				}
			}
			if (x < 0 || x > w) {
				ny = nx;
				dir = -dir;
				if (dir == 1) {
					x = 0;
				} else {
					x = w;
				}
			}
			int y = 0;
			for (int j = ny; j < r.size(); j++) {
				if (rx[j] + r[j].first > x - r[i].first &&
				    rx[j] - r[j].first < x + r[i].first) {
					y = max(y, r[i].first + ry[j] + r[j].first);
				}
			}
			if (y > h) {
				cout << "ERROR!" << endl;
			}
			rx[i] = x;
			ry[i] = y;
			nx = i;
		}

		vector <int> retx(N);
		vector <int> rety(N);
		for (int i = r.size() - 1; i >= 0; i--) {
			if (w == W) {
				retx[r[i].second] = rx[i];
				rety[r[i].second] = ry[i];
			} else {
				retx[r[i].second] = ry[i];
				rety[r[i].second] = rx[i];
			}
		}
		cout << "Case #" << caseno << ":";
		for (int i = 0; i < r.size(); i++) {
			cout << " " << retx[i] << " " << rety[i];
		}
		cout << endl;
	}

	return 0;
}
