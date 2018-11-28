#include <cstdio>
#include <string>
#include <iostream>
#include <vector>
using namespace std;

#define forn(i, n) for (i = 0; i < (int)(n); ++i)

int d[2][20];

int f1(int k, int p)
{
	int i, j, l;
	for (i = 0; i <= k; ++i) {
		for (j = 0; j <= k; ++j) {
			l = k - i - j;
			if (i >= 0 && j >= 0 && l >= 0 && max(abs(i - j), max( abs(i - l), abs(j - l))) < 2 && max(i, max(j, l)) >= p)
				return true;
		}
	}
	return false;
}

int f2(int k, int p)
{
	int i, j, l;
	for (i = 0; i <= k; ++i) {
		for (j = 0; j <= k; ++j) {
			l = k - i - j;
			if (i >= 0 && j >= 0 && l >= 0 && max(abs(i - j), max( abs(i - l), abs(j - l))) == 2 && max(i, max(j, l)) >= p)
				return true;
		}
	}
	return false;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output2.txt", "w", stdout);

	int t, i, tmp, k;
	cin >> t;
	forn(i, t) {
		if (i == 14) {
			int dbg = 1;
			++dbg;
		}
		int n, s, p, j;
		cin >> n >> s >> p;
		memset(d, -1, sizeof(d));
		d[0][0] = 0;
		forn(j, n) {
			cin >> tmp;
			memset(d[1], -1, sizeof(d[1]));
			for (k = 0; k <= s; ++k) {
				if (d[0][k] == -1)
					continue;
				int r1 = f1(tmp, p);
				d[1][k] = max(d[1][k], d[0][k] + r1);
				if (k < s && tmp >= 2 && tmp <= 28)
					d[1][k + 1] = max(d[1][k + 1], d[0][k] + f2(tmp, p));
			}
			for (k = 0; k <= s; ++k)
				d[0][k] = d[1][k];
		}
		cout << "Case #" << i + 1 << ": " << d[0][s] << endl;
	}

	return 0;
}