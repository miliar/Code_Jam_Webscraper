#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

int n, k;
vector< string > p, r;

void rotate() {
	r.clear();
	for (int i = 0;i < n;i++) {
		r.push_back("");
		for (int j = 0;j < n;j++) {
			r[i] += "*";
		}
	}
	for (int i = 0;i < n;i++) {
		for (int j = 0;j < n;j++) {
			r[j][n - i - 1] = p[i][j];
		}
	}
	for (int i = n - 1;i >= 0;i--) {
		for (int j = 0;j < n;j++) {
			int w = i;
			while (w < n - 1 && r[w + 1][j] == '.') {
				swap(r[w][j], r[w + 1][j]);
				w++;
			}
		}
	}
}

bool diagonal_one(int x, int y, char p) {
	int q;
	while (x < n && y < n) {
		if (r[x][y] != p) {
			x++, y++;
			continue;
		}
		if (x == 0 || y == 0 || r[x][y] != r[x - 1][y - 1]) {
			q = 1;
		}
		else {
			q++;
		}
		if (q >= k) {
			return true;
		}
		x++, y++;
	}
	return false;
}

bool diagonal_two(int x, int y, char p) {
	int q;
	while (x < n && y >= 0) {
		if (r[x][y] != p) {
			x++, y--;
			continue;
		}
		if (x == 0 || y == n - 1 || r[x][y] != r[x - 1][y + 1]) {
			q = 1;
		}
		else {
			q++;
		}
		if (q >= k) {
			return true;
		}
		x++, y--;
	}
	return false;
}

bool win(char p) {
	for (int x = 0;x < n;x++) {
		int q;
		for (int y = 0;y < n;y++) {
			if (r[x][y] != p)
				continue;
			if (y == 0 || r[x][y] != r[x][y - 1]) {
				q = 1;
			}
			else {
				q++;
			}
			if (q >= k) {
				return true;
			}
		}
	}
	for (int y = 0;y < n;y++) {
		int q;
		for (int x = 0;x < n;x++) {
			if (r[x][y] != p)
				continue;
			if (x == 0 || r[x][y] != r[x - 1][y]) {
				q = 1;
			}
			else {
				q++;
			}
			if (q >= k) {
				return true;
			}
		}
	}
	for (int i = 0;i < n;i++) {
		if (diagonal_one(i, 0, p) || diagonal_two(i, n - 1, p)) {
			return true;
		}
	}
	for (int i = 0;i < n;i++) {
		if (diagonal_one(0, i, p) || diagonal_two(0, i, p)) {
			return true;
		}
	}
	return false;
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("test.out", "w", stdout);
	int test;
	string x;
	cin >> test;
	for (int testID = 0;testID < test;testID++) {
		cin >> n >> k;
		p.clear();
		for (int i = 0;i < n;i++) {
			cin >> x;
			p.push_back(x);
		}
		rotate();
		bool c1 = win('R'), c2 = win('B');
		if (!c1 && !c2) {
			cout << "Case #" << testID + 1 << ": " << "Neither" << endl;
		}
		else if (c1 && c2) {
			cout << "Case #" << testID + 1 << ": " << "Both" << endl;
		}
		else if (c1) {
			cout << "Case #" << testID + 1 << ": " << "Red" << endl;
		}
		else {
			cout << "Case #" << testID + 1 << ": " << "Blue" << endl;
		}
	}
	return 0;
}
