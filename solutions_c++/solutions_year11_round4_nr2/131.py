#include <iostream>
#include <cstdio>
using namespace std;

#define MAXN 512

typedef long long tint;

int R, C;
tint m[MAXN][MAXN], sm[MAXN][MAXN], x[MAXN][MAXN], y[MAXN][MAXN];

tint x_cm(int px, int py, int k) {
	return x[px][py] - x[px-k][py] - x[px][py-k] + x[px-k][py-k] - px*(m[px][py] + m[px][py-k+1]) - (px-k+1)*(m[px-k+1][py] + m[px-k+1][py-k+1]);
}

tint y_cm(int px, int py, int k) {
	return y[px][py] - y[px-k][py] - y[px][py-k] + y[px-k][py-k] - py*(m[px][py] + m[px-k+1][py]) - (py-k+1)*(m[px][py-k+1] + m[px-k+1][py-k+1]);
}

tint mt(int px, int py, int k) {
	return sm[px][py] - sm[px-k][py] - sm[px][py-k] + sm[px-k][py-k] - m[px][py] - m[px-k+1][py] - m[px][py-k+1] - m[px-k+1][py-k+1];
}

bool check(int k) {
	int i, j;

	for (i=k; i<=R; i++) {
		for (j=k; j<=C; j++) {
			if (mt(i, j, k)*(2*i - k + 1) == 2*x_cm(i, j, k) && mt(i, j, k)*(2*j - k + 1) == 2*y_cm(i, j, k)) return true;
		}
	}
	return false;
}

int main() {

freopen("in.txt", "r", stdin);

int i, j, k, t, T;
tint D;
char tmpc;

cin >> T;

for (t=1; t<=T; t++) {

cin >> R;
cin >> C;
cin >> D;

for (i=1; i<=R; i++) {
	for (j=1; j<=C; j++) {
		cin >> tmpc;
		m[i][j] = D + tmpc-'0';

		x[i][j] = i*m[i][j];
		y[i][j] = j*m[i][j];
		sm[i][j] = m[i][j];
	}
}
for (i=0; i<=R+1; i++) sm[i][0] = x[i][0] = y[i][0] = 0;
for (j=0; j<=C+1; j++) sm[0][j] = x[0][j] = y[0][j] = 0;

for (i=1; i<=R; i++) {
	for (j=1; j<=C; j++) {
		sm[i][j] += sm[i][j-1];
		x[i][j] += x[i][j-1];
		y[i][j] += y[i][j-1];
	}
}

for (i=1; i<=R; i++) {
	for (j=1; j<=C; j++) {
		sm[i][j] += sm[i-1][j];
		x[i][j] += x[i-1][j];
		y[i][j] += y[i-1][j];
	}
}

for (k=min(R, C); k>=3; k--) {
	if (check(k) == true) break;
}

cout << "Case #" << t << ": ";
if (k == 2) cout << "IMPOSSIBLE" << endl;
else cout << k << endl;

}

return 0;
}
