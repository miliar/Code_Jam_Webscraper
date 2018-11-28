#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cfloat>
#include <numeric>

using namespace std;

const int oo = 0x3f3f3f3f;
const double eps = 1e-9;

typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;

#define sz(c) int((c).size())
#define all(c) (c).begin(), (c).end()
#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define FORD(i,a,b) for (int i = int(b)-1; i >= (a); i--)
#define FORIT(i,c) for (__typeof__((c).begin()) i = (c).begin(); i != (c).end(); i++)

int T, N, X[3000], H[3000];

bool rek(int a, int b, int s) {
	if (a >= b) return true;
	H[a] = H[b] - (b-a) * s;
	int pos = a;
	while (pos < b) {
		int nu = X[pos];
		if (nu > b) return false;
		if (nu < b) H[nu] = H[b] - (b-nu) * s;
		if (!rek(pos+1, nu, s+1)) return false;
		pos = nu;
	}
	return true;
}

int main() {
	cin >> T;
	FOR(cs, 1, T+1) {
		cin >> N;
		FOR(i, 0, N-1) cin >> X[i];
		FOR(i, 0, N-1) X[i]--;
		H[N-1] = 1000000000;
		cout << "Case #" << cs << ":";
		if (rek(0, N-1, 0)) {
			FOR(i, 0, N) cout << " " << H[i];
			cout << endl;
		} else {
			cout << " Impossible" << endl;
		}
	}
	return 0;
}
