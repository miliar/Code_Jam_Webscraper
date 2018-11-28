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

void testcase(int ncase) {
	int pos[] = { 1, 1 }, last[] = { 0, 0 }, T = 0, N;
	scanf("%d", &N);
	while (N--) {
		char c[2];
		int x;
		scanf("%s%d", c, &x);
		int ind = (c[0] == 'O'), dt = abs(pos[ind] - x)+1;
		pos[ind] = x;
		T = max(T+1, last[ind]+dt); 
		last[ind] = T;
	}
	printf("Case #%d: %d\n", ncase, T);
}

int main() {
	int T;
	scanf("%d", &T);
	FOR(i, 1, T) testcase(i);
}
