#include <cstdio>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

bool isValid(int x, int y, int k)
{
	if (x >= max(k - 1 - y, -(k - 1) + y) &&
	    x <= min(k - 1 + y, 3 * (k - 1) - y) &&
	    (x + y + k) % 2 == 1) {
		return true;
	}
	return false;
}

int ElegantDiamond(int k, vector <string> diamond)
{
	int mincx = 100;
	for (int cx = 0; cx < 2 * k - 1; cx++) {
		bool flag = true;
		for (int y = 0; y < 2 * k - 1; y++) {
			for (int x1 = 0; x1 < 2 * k - 1; x1++) {
				int x2 = 2 * cx - x1;
				if (isValid(x1, y, k) && isValid(x2, y, k) &&
				    diamond[y][x1] != diamond[y][x2]) {
					flag = false;
					break;
				}
			}
		}
		if (flag) {
			//cout << "x: " << cx << endl;
			if (max(k - 1 - cx, -(k - 1) + cx) <= mincx) {
				mincx = max(k - 1 - cx, -(k - 1) + cx);
			}
		}
	}
	int mincy = 100;
	for (int cy = 0; cy < 2 * k - 1; cy++) {
		bool flag = true;
		for (int x = 0; x < 2 * k - 1; x++) {
			for (int y1 = 0; y1 < 2 * k - 1; y1++) {
				int y2 = 2 * cy - y1;
				if (isValid(x, y1, k) && isValid(x, y2, k) &&
				    diamond[y1][x] != diamond[y2][x]) {
					flag = false;
					break;
				}
			}
		}
		if (flag) {
			//cout << "y: " << cy << endl;
			if (max(k - 1 - cy, -(k - 1) + cy) <= mincy) {
				mincy = max(k - 1 - cy, -(k - 1) + cy);
			}
		}
	}
	
	return (k + mincx + mincy) * (k + mincx + mincy) - k * k;
}

int main()
{
	string line;

	int cases;
	cin >> cases;
	getline(cin, line);

	for (int caseno = 1; caseno <= cases; caseno++) {
		int k;
		cin >> k;
		getline(cin, line);
		vector <string> diamond(2 * k - 1);
		for (int i = 0; i < 2 * k - 1; i++) {
			getline(cin, diamond[i]);
		}

		int ret = ElegantDiamond(k, diamond);

		cout << "Case #" << caseno << ": " << ret << endl;
	}

	return 0;
}
