#include <queue>
#include <sstream>
#include <iostream>
#include <iterator>
#include <algorithm>
#include <utility>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <cmath>
using namespace std;

#define SZ(x) (int)((x).size())
#define FOR(i, a, b) for(typeof(a) i = (a); i < (b); ++i)
#define FORE(i, x) for(typeof((x).begin()) i=(x).begin(); i != (x).end(); ++i)
#define PB push_back
#define MK make_pair
#define FI first
#define SE second
#define ALL(x) (x).begin(),(x).end()

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<vector<int> > VVI;
typedef pair<int,int> PII;
typedef vector<PII> VPI;

int main() {
	int T, n, a, b;
	scanf("%d", &T);
	for (int kase = 0; kase < T; ++kase) {
		int ret = 0;
		scanf("%d", &n);
		vector<PII> v;
		for (int i = 0; i < n; ++i) {
			scanf("%d%d", &a, &b);
			v.PB(MK(a,b));
		}
		sort(v.begin(), v.end());
		for (int i = 0; i < n; ++i) {
			for (int j = i + 1; j < n; ++j) {
				if (v[i].SE > v[j].SE) ret ++;
			}
		}
		printf("Case #%d: %d\n", kase + 1, ret);
	}
	return 0;
}


