#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <set>
#include <map>
#include <bitset>
#include <valarray>
#include <algorithm>
#include <functional>
#include <numeric>
#include <complex>
#include <utility>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
using namespace std;

#define REP(i, n) for (int i = 0; i < (n); i++)
#define FOR(i, a, b) for (int i = (a); i <= (b); i++)
#define FORD(i, a, b) for (int i = (a); i >= (b); i--)
#define FORC( it, V ) for( __typeof( (V).begin() ) it = (V).begin(); it != (V).end(); ++it )
#define SZ(a) a.size()
#define INF 10000000

int n, ex;
int gate[11111];
int change[11111];
int f[11111][2];

void read_data() {
	cin >> n >> ex;
	FOR(i, 1, (n - 1) / 2) {
		cin >> gate[i] >> change[i];
	}
	FOR(x, (n - 1) / 2 + 1, (n - 1) / 2 + (n + 1) / 2) {
		int z;
		cin >> z;
		f[x][0] = f[x][1] = INF;
		f[x][z] = 0;
	}
}

void dp(int i) {
	if (i > (n - 1) / 2) return;
//	cout << i << " " << gate[i] << " " << change[i] << endl;
	int i1 = i * 2;
	int i2 = i * 2 + 1;
	f[i][0] = INF;
	f[i][1] = INF;
	dp(i1);
	dp(i2);	
	FOR(x1, 0, 1) FOR(x2, 0, 1) {
		if (gate[i] == 1) 
			f[i][(x1 & x2)] <?= f[i1][x1] + f[i2][x2];
		else 
			f[i][(x1 | x2)] <?= f[i1][x1] + f[i2][x2];
	}
	if (!change[i]) return;
	gate[i] = 1 - gate[i];	
	FOR(x1, 0, 1) FOR(x2, 0, 1) {
		if (gate[i] == 1) 
			f[i][(x1 & x2)] <?= f[i1][x1] + f[i2][x2] + 1;
		else 
			f[i][(x1 | x2)] <?= f[i1][x1] + f[i2][x2] + 1;
	}
}

int main() {
	int test;
	cin >> test;
	FOR(i, 1, test) {
		cout << "Case #" << i << ": ";
		read_data();
		dp(1);
		if (f[1][ex] < INF) cout << f[1][ex] << endl;
		else cout << "IMPOSSIBLE" << endl;
	}
	return 0;
};

