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

bool oppose[256][256];
char combine[256][256];

const int NMAX = 100;
char T[NMAX+1], res[NMAX];

void testcase(int ncase) {
	REP(i, 256) fill_n(oppose[i], 256, false);
	REP(i, 256) fill_n(combine[i], 256, 0);
	{
		int C;
		scanf("%d", &C);
		REP(i, C) {
			static char tmp[5];
			scanf("%s", tmp);
			combine[(int)tmp[0]][(int)tmp[1]] = combine[(int)tmp[1]][(int)tmp[0]] = tmp[2];
		}
		int D;
		scanf("%d", &D);
		REP(i, D) {
			static char tmp[5];
			scanf("%s", tmp);
			oppose[(int)tmp[0]][(int)tmp[1]] = oppose[(int)tmp[1]][(int)tmp[0]] = true;
		}
	}
	
	int N, top = 0;
	scanf("%d%s", &N, T);
	REP(ind, N) {
		res[top++] = T[ind];
		if (top >= 2 && combine[(int)res[top-1]][(int)res[top-2]]) {
			res[top-2] = combine[(int)res[top-1]][(int)res[top-2]];
			--top;
		} else {
			FOR(k, 0, top-2) if (oppose[(int)res[k]][(int)res[top-1]]) {
				top = 0;
				break;
			}
		}
	}
	printf("Case #%d: [", ncase);
	FOR(k, 0, top-2) printf("%c, ", res[k]);
	if (top > 0) printf("%c", res[top-1]);
	printf("]\n");
}

int main() {
	int T;
	scanf("%d", &T);
	FOR(i, 1, T) testcase(i);
}
