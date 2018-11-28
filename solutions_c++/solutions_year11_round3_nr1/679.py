#include <iostream>
#include <stdio.h>
#include <math.h>
#include <algorithm>
#include <string>
#include <climits>

#define MAX_SIZE 111111

using namespace std;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int test = 0;
	int test_count;

	cin >> test_count;

	while (test < test_count) {
		test++;

		int n, m;
		cin >> n >> m;
		
		char a[55][55];

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				cin >> a[i][j];
			}
		}


		for (int i = 0; i < n-1; i++) {
			for (int j = 0; j < m-1; j++) {
				if (a[i][j] == '#' && a[i+1][j] == '#' && a[i][j+1] == '#' && a[i+1][j+1] == '#') {
					a[i][j] = '/';
					a[i+1][j] = '\\';
					a[i][j+1] = '\\';
					a[i+1][j+1] = '/';
				}
			}
		}

		bool has_sharp = false;
		
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (a[i][j] == '#') {
					has_sharp = true;
				}
			}
		}

		cout << "Case #" << test << ":" << endl;

		if (! has_sharp) {
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < m; j++) {
					cout << a[i][j];
				}
				cout << endl;
			}
		} else {
			cout << "Impossible" << endl;
		}
	}

	return 0;
}