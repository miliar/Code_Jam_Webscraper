#include <iostream>
#include <cstdio>

using namespace std;

int m, n;
char a[55][55];

bool empty() {
	for (int i = 0; i < m; i++)
		for (int j = 0; j < n; j++)
			if (a[i][j] == '#')
				return false;
	return true;
}

void solve(int test) {
	cout << "Case #" << test << ":" << endl;
	cin >> m >> n;
	for (int i = 0; i < m; i++)
		cin >> a[i];
	while (!empty()) {
		bool find = false;
		for (int i = 0; i + 1 < m; i++)
			for (int j = 0; j + 1 < n; j++)
				if (a[i][j] == '#' && a[i][j + 1] == '#' && a[i + 1][j] == '#'
						&& a[i + 1][j + 1] == '#') {
					a[i][j] = '/';
					a[i][j + 1] = '\\';
					a[i + 1][j] = '\\';
					a[i + 1][j + 1] = '/';
					find = true;
					goto gate;
				}
		gate: if (!find) {
			cout << "Impossible" << endl;
			return;
		}
	}
	for (int i = 0; i < m; i++)
		cout << a[i] << endl;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int nTest;
	cin >> nTest;

	for (int i = 0; i < nTest; i++)
		solve(i + 1);

	return 0;
}
