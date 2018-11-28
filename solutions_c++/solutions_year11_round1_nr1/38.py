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

ll T, N, PD, PG;

ll gcd(ll a, ll b) {
	return (b == 0) ? a : gcd(b, a%b);
}

bool check() {
	if (PD < 100 && PG == 100) return false;
	if (PD > 0 && PG == 0) return false;
	ll g = gcd(PD, 100);
	return N >= 100/g;
}

int main() {
	cin >> T;
	FOR(cs, 1, T+1) {
		cin >> N >> PD >> PG;
		if (check()) {
			cout << "Case #" << cs << ": Possible" << endl;
		} else {
			cout << "Case #" << cs << ": Broken" << endl;
		}
	}
	return 0;
}
