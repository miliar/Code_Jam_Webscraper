#include <iostream>
using namespace std;

char a[50][50];
int n, m;

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);

	int task; cin >> task;
	for (int tt = 1; tt <= task; ++tt) {
		cout << "Case #" << tt << ":" << endl;
		cin >> n >> m; int s = 0;
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < m; ++j) {
				cin >> a[i][j]; s += a[i][j] == '#';
			}
		bool f = 1;
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < m; ++j)
				if (a[i][j] == '#')
					if (i == n || j == m || a[i + 1][j] != '#' || a[i][j + 1] != '#' || a[i + 1][j + 1] != '#') {
						f = 0; break;
					}
					else {
						a[i][j] = 47; a[i][j + 1] = 92;
						a[i + 1][j] = 92; a[i + 1][j + 1] = 47;
					}
		if (!f) cout << "Impossible" << endl;
		else 
			for (int i = 0; i < n; ++i) {
				for (int j = 0; j < m; ++j)
					cout << a[i][j];
				cout << endl;
		}
	}
	return 0;
}

