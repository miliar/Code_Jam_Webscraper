#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <map>
#include <numeric>
#include <set>
#include <string>
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

const int INF = 1000000000;

const int NMAX = 1000, LOGMAX = 20;

int T[NMAX];

void testcase(int ncase) {
	int N;
	scanf("%d", &N);
	REP(i, N) scanf("%d", T+i);

	REP(bit, LOGMAX) {
		int cnt = 0;
		REP(i, N) if (T[i] & (1<<bit))
			++cnt;
		if (cnt%2 == 1) {
			printf("Case #%d: NO\n", ncase);
			return;
		}
	}
	printf("Case #%d: %d\n", ncase, accumulate(T, T+N, -*min_element(T, T+N)));
}

int main() {
	int T;
	scanf("%d", &T);
	FOR(i, 1, T) testcase(i);
}
