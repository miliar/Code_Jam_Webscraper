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

string i2s(int x) { ostringstream tmp;  tmp << x;  return tmp.str(); }
int s2i(string s) { istringstream i(s);  int x;  i >> x;  return x; } 

const int dx[2] = {2, 1};
const int dy[2] = {1, 2};

int f[111][111];
int M, N, K;

void read_data() {
	memset(f, 0, sizeof(f));
	cin >> M >> N >> K;
	REP(i, K) {
		int u, v;
		cin >> u >> v;
		f[u][v] = -1;
	}
}

void process() {
	f[1][1] = 1;
	FOR(sum, 2, M + N) 
	FOR(i, 1, M) {
		int j = sum - i;
		if (1 <= j && j <= N && f[i][j] != -1) {
			REP(x, 2) {
				int ii = i - dx[x];
				int jj = j - dy[x];
				if (1 <= ii && ii <= M && 1 <= jj && jj <= N && f[ii][jj] != -1) {
					f[i][j] += f[ii][jj];
					f[i][j] %= 10007;
				}
			}
		}
	}
	cout << f[M][N] << endl;
}

int main() {
	int test;
	cin >> test;
	FOR(i, 1, test) {
		cout << "Case #" << i << ": ";		
		read_data();
//		cout << M << " " << N << " " << K << endl;
		process();
	}
	return 0;
};

