// C++11

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
#include <unordered_map>
#include <unordered_set>
#include <tuple>
using namespace std;


typedef long double ld;
typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;

const int oo = 0x3f3f3f3f;
const double eps = 1e-9;

#define sz(c) int((c).size())
#define all(c) (c).begin(), (c).end()
#define FOR(i,a,b) for(int i = (a); i < (b); i++)
#define FORD(i,a,b) for(int i = int(b)-1; i >= (a); i--)
#define FORIT(i,c) for(__typeof__((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define pb push_back
#define mp make_pair

int main () {
	int T;
	cin >> T;

	FOR(t,1,T+1) {
		int A, B, x, cnt = 0;
		cin >> A >> B;

		FOR(i,A,B+1) {
			stringstream ss;
			set<int> seen;
			ss << i;
			FOR(p,1,sz(ss.str())) {
				stringstream ss2;
				if (ss.str()[p] == '0') continue;
				ss2 << ss.str().substr(p) << ss.str().substr(0,p);
				ss2 >> x;
				if (i < x && x < B+1)  seen.insert(x);
			}
			cnt += sz(seen);
		}

		cout << "Case #" << t << ": " << cnt << endl;
	}

	return 0;
}
