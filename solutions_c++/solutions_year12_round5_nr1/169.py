#include <list>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <cfloat>
#include <climits>
#include <numeric>
#include <ctime>
#include <limits>

using namespace std;

const int oo = 0x3f3f3f3f;
const double eps = 1e-9;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef pair<string,int> psi;
typedef vector<ll> vll;
typedef vector<int> vi;
typedef vector<string> vs;

#define sz(c) int((c).size())
#define all(c) (c).begin(), (c).end()
#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define FORS(i,a,b,s) for (int i = (a); i < (b); i=i+(s))
#define FORD(i,a,b) for (int i = int(b)-1; i >= (a); i--)
#define FORIT(i,c) for (__typeof__((c).begin()) i = (c).begin(); i != (c).end(); i++)

struct str {
	int idx;
	int l;
	double p;

	bool operator< (const str& o) const {
		int a = 100*l*p + (l+o.l)*(100-p)*o.p;
		int b = 100*o.l*o.p + (o.l+l)*(100-o.p)*p;
		return a<b;
	}
};

str s[1000];

int main() {
	int tc;
	cin >> tc;
	FOR(ctc,1,tc+1) {
		cout << "Case #" << ctc << ":";
		int n;
		cin >> n;
		FOR(i,0,n)
			cin >> s[i].l, s[i].idx = i;
		FOR(i,0,n)
			cin >> s[i].p, s[i].idx = i;
		stable_sort(s,s+n);
		FOR(i,0,n) {
			cout << " " << s[i].idx;
		}
		cout << endl;
	}
	return 0;
}
