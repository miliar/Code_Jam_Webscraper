#include <iostream>
#include <cstdio>

using namespace std;

#define MAXN 100

int n;
char a[MAXN + 5][MAXN + 5];
double wp[MAXN + 5], owp[MAXN + 5], oowp[MAXN + 5], r[MAXN + 5];

void solve(int test) {
	cin >> n;

	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			cin >> a[i][j];

	for (int i = 0; i < n; i++) {
		int k, l;
		k = l = 0;
		for (int j = 0; j < n; j++) {
			if (a[i][j] != '.')
				l++;
			if (a[i][j] == '1')
				k++;
		}
		wp[i] = k * 1.0 / l;
	}

	for (int i = 0; i < n; i++) {
		int l = 0;
		double s = 0;
		for (int j = 0; j < n; j++) {
			if (a[i][j] == '.')
				continue;
			l++;
			int x, y;
			x = y = 0;
			for (int k = 0; k < n; k++)
				if (k != i && a[j][k] != '.') {
					if (a[j][k] == '1')
						x++;
					y++;
				}
			s += x * 1.0 / y;
		}
		owp[i] = s / l;
	}

	for (int i = 0; i < n; i++) {
		int l = 0;
		double s = 0;
		for (int j = 0; j < n; j++)
			if (a[i][j] != '.') {
				l++;
				s += owp[j];
			}
		oowp[i] = s / l;
	}

	for (int i = 0; i < n; i++)
		r[i] = 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i];

	//	for (int i = 0; i < n; i++)
	//		cout << wp[i] << ' ';
	//	cout << endl;
	//	for (int i = 0; i < n; i++)
	//		cout << owp[i] << ' ';
	//	cout << endl;
	//	for (int i = 0; i < n; i++)
	//		cout << oowp[i] << ' ';
	//	cout << endl;
	cout << "Case #" << test << ":" << endl;
	for (int i = 0; i < n; i++)
		printf("%.12lf\n", r[i]);
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int nTest;
	cin >> nTest;

	for (int i = 0; i < nTest; i++) {
		solve(i + 1);
	}

	return 0;
}
