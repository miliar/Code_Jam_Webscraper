#include <iostream>

using namespace std;

const int smax = 100, mod = 10007;
int d[smax][smax];
bool c[smax][smax];

int main() {
	int nt, it;
	
	cin >> nt;
	for (it = 1; it <= nt; it++) {
		int h, w, r, i, y, x;
		
		memset(c, 0, sizeof c);
		memset(d, 0, sizeof d);
		cin >> h >> w >> r;
		for (i = 0; i < r; i++) {
			cin >> y >> x; y--, x--;
			c[y][x] = true;
		}
		d[0][0] = 1;
		for (y = 0; y < h; y++) {
			for (x = (y ? 0 : 1); x < w; x++) if (!c[y][x]) {
				d[y][x] = ((y >= 2 && x >= 1 ? d[y - 2][x - 1] : 0) + (y >= 1 && x >= 2 ? d[y - 1][x - 2] : 0)) % mod;
			}
		}
		
		cout << "Case #" << it << ": " << d[h - 1][w - 1] << '\n';
	}
	
	return 0;
}
