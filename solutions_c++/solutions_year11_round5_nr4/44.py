#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <algorithm>
#include <functional>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

#define REP(i, n) for (int i = 0, _n = (n); i < _n; ++i)
#define FOR(i, a, b) for (int i = (a), _n = (b); i <= _n; ++i)
#define FORD(i, a, b) for (int i = (a), _n = (b); i >= _n; --i)
#define FORE(it, c) for(__typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)
#define ALL(c) (c).begin(), (c).end()
#define PB push_back
#define MP make_pair
#define FI first
#define SE second

typedef long long LL;
typedef pair<int,int> PII;
typedef vector<int> VI;

const int PMAX = 400;

const int INF = 1000000000;

char buf[1000];

LL pot[70];
int Q[50];


void testcase() {
	scanf("%s", buf);
	const int N = strlen(buf);
	
	int NQ = 0;
	REP(i, N) if (buf[i] == '?') Q[NQ++] = i;
	
	LL base = 0;
	REP(i, N) {
		base *= 2;
		if (buf[i] == '1') ++base;
	}
	
	REP(zb, 1<<NQ) {
		LL cur = base;
		int a = zb;
		REP(i, NQ) {
			if (a%2 == 1) 
				cur += pot[N-1-Q[i]];
			a /= 2;
		}
		
		LL res = sqrtl(cur);
		if (res*res == cur) {
			a = zb;
			REP(i, NQ) {
				buf[Q[i]] = '0' + (a%2==1);
				a /= 2;
			}
			printf("%s\n", buf);
			return;
		}
	}
}

int main() {
	REP(i, 70) pot[i] = (1LL<<i);

	int T;
	scanf("%d", &T);
	FOR(i, 1, T) {
		printf("Case #%d: ", i);
		testcase();
	}
}
