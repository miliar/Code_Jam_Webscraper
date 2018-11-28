#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;
vector<string> a;
int n, m;

int main() {
	int testCnt;
	cin >> testCnt;

	for (int T = 1; T <= testCnt; ++T) {
		cout << "Case #" << T << ": " << endl;
		cin >> n >> m;
		a.clear();
		for (int i = 0; i < n; ++i) {
			string s;
			cin >> s;
			a.push_back(s);
		}
		bool fl = true;
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < m; ++j) {
				if (a[i][j] == '#') {
					if (i+1 < n && j+1 < m && a[i+1][j] == '#' && a[i][j+1] == '#' && a[i+1][j+1] == '#') {
						a[i][j] = '/'; a[i][j+1] = '\\';
						a[i+1][j] = '\\'; a[i+1][j+1] = '/';
					} else
						fl = false;
				}
			}
		}
		if (!fl)
			cout << "Impossible" << endl;
		else
			for (int i = 0; i < n; ++i)
				cout << a[i] << endl;

	}

	return 0;
}