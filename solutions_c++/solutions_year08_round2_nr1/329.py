/*
FROM: GCJ (Google Code Jam) Round 1B 2008
PROB: A Crop Triangles

LANG: GNU C++ (g++ (GCC) 4.3.1 20080612 (Red Hat 4.3.1-2))
OPT: -lm -O2
*/


#include <cstdio>
#include <cstring>

typedef long long ll;

int ma3x[3][3];

void clear_ma3x () {
	memset (ma3x, 0, sizeof (ma3x));
}

void fill_ma3x () {
	int n;
	int a, b, c, d;
	int x0, y0;
	int m;
	scanf ("%d", &n);
	scanf ("%d %d %d %d", &a, &b, &c, &d);
	scanf ("%d %d", &x0, &y0);
	scanf ("%d", &m);

	for (int i = 0; i < n; ++i) {
		++ma3x[x0 % 3][y0 % 3];
		x0 = ((ll)a * x0 + b) % m;
		y0 = ((ll)c * y0 + d) % m;
	}
}

bool good (int ii, int jj, int kk) {
	int x = ii / 3 + jj / 3 + kk / 3;
	int y = ii % 3 + jj % 3 + kk % 3;
	return x % 3 == 0 && y % 3 == 0;
}

ll idx (int i) {
	return (ll)ma3x[i/3][i%3];
}

int main () {
	int tc;
	scanf ("%d", &tc);

	for (int ctc = 1; ctc <= tc; ++ctc) {
		clear_ma3x ();
		fill_ma3x ();

		ll times;
		ll res = 0;
		for (int ii = 0; ii < 9; ++ii)
			for (int jj = ii; jj < 9; ++jj) {
				for (int kk = jj; kk < 9; ++kk) {
					if (good(ii, jj, kk)) {
						if (ii == jj && jj == kk) {
							times = idx(ii) * (idx(ii) - 1) * (idx(ii) - 2) / 6;
						} else if (ii == jj) {
							times = idx(ii) * (idx(ii) - 1) * idx(kk) / 2;
						} else if (jj == kk) {
							times = idx(ii) * idx(jj) * (idx(jj) - 1) / 2;
						} else {
							times = idx(ii) * idx(jj) * idx(kk);
						}
						res += times;
					}
				}
			}
		printf ("Case #%d: %lld\n", ctc, res);
	}
	return 0;
}
