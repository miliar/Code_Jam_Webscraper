#include <iostream>

using namespace std;

char a[50][50];

int main() {
	int t;
	cin >> t;
	for (int caseno = 1; caseno <= t; caseno++) {
		int n,k;
		cin >> n >> k;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				cin >> a[i][j];
			}
		}
		for (int i = 0; i < n; i++) {
			int x = n-1;
			for (int j = n-1; j >= 0; j--) {
				if (a[i][j] != '.') {
					a[i][x] = a[i][j];
					if (x != j)
						a[i][j] = '.';
					x--;
				}
			}
		}
// 		for (int i = 0; i < n; i++) {
// 			for (int j = 0; j < n; j++) {
// 				cout << a[i][j];
// 			}
// 			cout << endl;
// 		}
		bool r = false;
		bool b = false;
		for (int i = n-1; i >= 0; i--) {
			for (int j = n-1; j >= 0; j--) {
				if (!r && a[i][j] == 'R') {
					//go left
					int c = 1;
					int x = i;
					int y = j-1;
					while (y >= 0 && c < k && a[x][y] == 'R') {
						y--;
						c++;
					}
					if (c == k) {
						r = true;
						continue;
					}
					//go up left
					c = 1;
					x = i-1;
					y = j-1;
					while (x >= 0 && y >= 0 && c < k && a[x][y] == 'R') {
						y--;
						x--;
						c++;
					}
					if (c == k) {
						r = true;
						continue;
					}
					//go up
					c = 1;
					x = i-1;
					y = j;
					while (x >= 0 && c < k && a[x][y] == 'R') {
						x--;
						c++;
					}
					if (c == k) {
						r = true;
						continue;
					}
					//go up right
					c = 1;
					x = i-1;
					y = j+1;
					while (x >= 0 && y < n && c < k && a[x][y] == 'R') {
						y++;
						x--;
						c++;
					}
					if (c == k) {
						r = true;
						continue;
					}
				}
				if (!b && a[i][j] == 'B') {
					//go left
					int c = 1;
					int x = i;
					int y = j-1;
					while (y >= 0 && c < k && a[x][y] == 'B') {
						y--;
						c++;
					}
					if (c == k) {
						b = true;
						continue;
					}
					//go up left
					c = 1;
					x = i-1;
					y = j-1;
					while (x >= 0 && y >= 0 && c < k && a[x][y] == 'B') {
						y--;
						x--;
						c++;
					}
					if (c == k) {
						b = true;
						continue;
					}
					//go up
					c = 1;
					x = i-1;
					y = j;
					while (x >= 0 && c < k && a[x][y] == 'B') {
						x--;
						c++;
					}
					if (c == k) {
						b = true;
						continue;
					}
					//go up right
					c = 1;
					x = i-1;
					y = j+1;
					while (x >= 0 && y < n && c < k && a[x][y] == 'B') {
						y++;
						x--;
						c++;
					}
					if (c == k) {
						b = true;
						continue;
					}
				}
			}
		}
		cout << "Case #" << caseno << ":  ";
		if (r && b)
			cout << "Both";
		else if (r)
			cout << "Red";
		else if (b)
			cout << "Blue";
		else
			cout << "Neither";
		cout << endl;
	}
}