#include <iostream>
#include <algorithm>

using namespace std;


int main() {
	int ncases;
	cin >> ncases;
	for (int caseno = 1; caseno <= ncases; caseno++) {
		int nrects;
		cin >> nrects;
		int bd[105][105];
		fill(bd[0], bd[105], 0);
		for (int i = 0; i < nrects; i++) {
			int x1, x2, y1, y2;
			cin >> x1 >> y1 >> x2 >> y2;
			if (x1 > x2) swap(x1, x2);
			if (y1 > y2) swap(y1, y2);
			for (int x = x1; x <= x2; x++)
				for (int y = y1; y <= y2; y++)
					bd[x][y] = 1;
		}
		int t = 0;
		int done = false;
		while (!done) {
			t++;
			done = true;
			for (int i = 101; i > 0; i--)
				for (int j = 101; j > 0; j--) {
					bd[i][j] = bd[i][j] ? bd[i - 1][j] || bd[i][j - 1]
						: bd[i - 1][j] && bd[i][j - 1];
					done &= !bd[i][j];
				}
		}
		cout << "Case #" << caseno << ": " << t << endl;
	}
	return 0;
}
