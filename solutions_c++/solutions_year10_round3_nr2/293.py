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

const double eps = 1e-8;

int main() {
	int T, n, l, p, c;
	scanf("%d", &T);
	for (int kase = 0; kase < T; ++kase) {
		int ret = 0;
		scanf("%d%d%d", &l, &p, &c);
		ret = (int)(ceil(log(1.*p/l)/log(c)) + eps);
		ret = (int)(ceil(log(ret)/log(2)) + eps);
		printf("Case #%d: %d\n", kase + 1, ret);
	}
	return 0;
}



