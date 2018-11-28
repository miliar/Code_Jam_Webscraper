#include <cstdio>
#include <iostream>

using namespace std;

int n;
double WP[110][110];
double OWP[110];
double OOWP[110];
char mat[110][110];

void init() {
	for(int i = 0; i < 110; ++i) {
		for(int j = 0; j < 110; ++j) {
			WP[i][j] = -10.;
		}
		OWP[i] = OOWP[i] = -10.;
	}
}

double getWP(int t, int e = -1) {
	if (WP[t][e+1] < -1.) {
		int win = 0, match = 0;
		for(int i = 0; i < n; ++i) {
			if (i == e || mat[t][i] == '.')
				continue;

			if (mat[t][i] == '1')
				++win;
			++match;
		}

		WP[t][e+1] = (double)win / (double)match;
	}
	return WP[t][e+1];
}

double getOWP(int t) {
	if (OWP[t] < -1.) {
		OWP[t] = 0.;
		int div = 0;
		for(int i = 0; i < n; ++i) {
			if (mat[t][i] == '.')
				continue;

			++div;
			OWP[t] += getWP(i, t);
		}

		OWP[t] /= (double)(div);
	}

	return OWP[t];
}

double getOOWP(int t) {
	if (OOWP[t] < -1.) {
		OOWP[t] = 0.;
		int div = 0;
		for(int i = 0; i < n; ++i) {
			if (mat[t][i] == '.')
				continue;

			++div;
			OOWP[t] += getOWP(i);
		}

		OOWP[t] /= (double)(div);
	}

	return OOWP[t];
}

void solve() {
	init();

	scanf("%d", &n);
	for(int i = 0; i < n; ++i) {
		scanf("%s", mat[i]);
	}

	for(int i = 0; i < n; ++i) {
		OWP[i] = getOWP(i);
	}

	for(int i = 0; i < n; ++i) {
		OOWP[i] = getOOWP(i);
	}

	for(int i = 0; i < n; ++i) {
		cout << 0.25 * getWP(i) + 0.50 * getOWP(i) + 0.25 * getOOWP(i) << endl;
	}
}

int main() {
	freopen("C:\\Users\\kiheon\\Downloads\\A-large.in", "r", stdin);
	freopen("c:\\users\\kiheon\\Downloads\\output.txt", "w", stdout);

	int c;
	scanf("%d", &c);
	cout.precision(12);
	for(int i = 1; i <= c; ++i) {
		cout << "Case #" << i << ':' << endl;
		solve();
	}

	return 0;
}
