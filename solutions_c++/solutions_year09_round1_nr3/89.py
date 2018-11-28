#include <iostream>
#include <vector>

using namespace std;

typedef long double ld;

ld ch[41][41];
int C, N;
ld dp[41];  //remaining #

ld choose(int a, int b) {
	if (a < b) return 0;
	return ch[a][b];
}

ld solve(int c) {
	if (dp[c] > -1) return dp[c];
	int i;
	if (c >= C) return 0;
	ld res = 1;
	for (i=N; i>=1; i--) {
		res += choose(C-c, i)/ch[C][N]*choose(c, N-i)*solve(c+i);
	}
	ld p = choose(C-c, 0)*choose(c, N)/ch[C][N];
	return dp[c] = res / (1-p);
}

int main () {
	int i, j;
	for (i=0; i<41; i++) {
		ch[i][0] = 1;
		ch[0][i] = 0;
	}
	ch[0][0] = 1;
	for (i=1; i<41; i++) {
		for (j=1; j<=i; j++) {
			ch[i][j] = ch[i-1][j] + ch[i-1][j-1];
		}
	}
	int T, cse=0;
	cin >> T;
	while (T--) {
		cin >> C >> N;
		for (i=0; i<41; i++) dp[i] = -2;
		ld r = solve(0);
		cout.setf(ios::fixed);
		cout.precision(7);
		cout << "Case #" << ++cse << ": " << r << endl;
		cerr << cse << endl;
	}
	return 0;
}
