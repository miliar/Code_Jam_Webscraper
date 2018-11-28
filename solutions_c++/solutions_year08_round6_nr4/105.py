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
#define INF 1000000000

int c1[55][55];
int c2[55][55];
bool found;
int n, m;
int a[55];
bool chua[55];

void read_data() {
	cin >> n;
	memset(c1, 0, sizeof(c1));
	memset(c2, 0, sizeof(c2));
	int u, v;
	REP(i, n - 1) {
		cin >> u >> v;
		c1[u][v] = 1;
		c1[v][u] = 1;
	}
	cin >> m;
	REP(i, m - 1) {
		cin >> u >> v;
		c2[u][v] = 1;
		c2[v][u] = 1;
	}
}

bool ok(int x) {
	FOR(i, 1, x) FOR(j, i + 1, x) if (c1[a[i]][a[j]] != c2[i][j]) {
		return false;
	}
	return true;
}

void duyet(int i) {
	if (!ok(i - 1)) return;
	if (i == m + 1) {
		cout << "YES" << endl;
		found = true;
		return;
	}
	FOR(j, 1, n) if (chua[j]) {
		chua[j] = false;
		a[i] = j;
		duyet(i + 1);
		if (found) return;
		chua[j] = true;
	}
}

void process() {
	found = false;
	memset(chua, true, sizeof(chua));
	duyet(1);
	if (!found) cout << "NO" << endl;
}

int main() {
    int notest;
    cin >> notest;
    FOR(i, 1, notest) {
		cout << "Case #" << i << ": ";
		
		read_data();
		process();
		
		
    }
    return 0;
}
