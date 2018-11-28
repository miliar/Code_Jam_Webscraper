#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <cassert>
#include <string>
#include <cstdio>
using namespace std;

int main() {
	int cn;
	cin >> cn;
	for (int tc = 1; tc <= cn; ++tc) {
		int n,m;
		cin >> n >> m;
		vector<string> f(n);
		for (int i = 0; i < n; ++i)
			cin >> f[i];
		bool bad = false;
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < m; ++j) {
				if (f[i][j] == '#') {
					if (i + 1 >= n || j + 1 >= m)
						bad = true;
					else {
						if (f[i+1][j] != '#' || f[i+1][j+1] != '#' || f[i][j+1] != '#') {
							bad = true;
						} else {
							f[i][j] = '/';
							f[i][j+1] = '\\';
							f[i+1][j] = '\\';
							f[i+1][j+1] = '/';
						}
					}
				}
			}
		}
		printf("Case #%d:\n", tc);
		if (bad)
			cout << "Impossible" << endl;
		else {
			for (int i = 0; i < n; ++i) {
				cout << f[i] << endl;
			}
		}
	}
	return 0;
}
