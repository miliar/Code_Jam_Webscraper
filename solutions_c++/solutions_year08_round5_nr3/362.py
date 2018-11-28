#include <algorithm>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <iostream>
#include <iterator>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>
using namespace std;

namespace tip {
template<class F, class S> ostream& operator<< (ostream& out, const pair<F, S>& p) {
	return out << "<" << p.first << " : " << p.second << ">";
}
template<class T> ostream& operator<< (ostream& out, const vector<T>& v) {
	for (int i = 0; i < static_cast<int>(v.size()); ++i)
		out << (i == 0 ? "(" : ", ") << v[i];
	return out << ")";
}
inline string function() {
	return "";
}
template<class T> inline string function(const T& x) {
	ostringstream oss;
	oss << " = " << x << ", ";
	return oss.str();
}
}

#define TIP_0(x, ...) #x << tip::function(x) << endl
#define TIP_1(x, ...) #x << tip::function(x) << TIP_0(__VA_ARGS__)
#define TIP_2(x, ...) #x << tip::function(x) << TIP_1(__VA_ARGS__)
#define TIP_3(x, ...) #x << tip::function(x) << TIP_2(__VA_ARGS__)
#define TIP_4(x, ...) #x << tip::function(x) << TIP_3(__VA_ARGS__)
#define TIP_5(x, ...) #x << tip::function(x) << TIP_4(__VA_ARGS__)
#define TIP_6(x, ...) #x << tip::function(x) << TIP_5(__VA_ARGS__)
#define TIP_7(x, ...) #x << tip::function(x) << TIP_6(__VA_ARGS__)
#define TIP_8(x, ...) #x << tip::function(x) << TIP_7(__VA_ARGS__)
#define TIP_9(x, ...) #x << tip::function(x) << TIP_8(__VA_ARGS__)
#define TIP(...) (cerr << __LINE__ << ": " << TIP_9(__VA_ARGS__))

#define REP(i, N) for (int i = 0; i < (int)(N); ++i)
#define FOR(i, N, M) for (int i = (int)(N); i <= (int)(M); ++i)
#define ALL(x) (x).begin(), (x).end()
#define CLEAR(X) (memset(X, 0, sizeof(X)))
#define SZ(x) ( (int) x.size() )
#define PB push_back

#define FORD(i, N, M) for (int i = (int)(N); i >= (int)(M); --i)
#define FORI(it, x) for (__typeof((x).begin()) it = (x).begin(); it != (x).end(); ++it)
#define MP make_pair
#define INF 0x3f3f3f3f
typedef long long LL;


int N, M;
char mat[128][128];
int best[16][2 * 1024];

void solve_case() {
    int sol = 0;
    char c;
    scanf("%d %d\n", &N, &M);
    CLEAR(best);
    REP(i, N) REP(j, M) {
        do { scanf("%c", &c); } while (c != '.' && c != 'x');
        mat[i + 1][j] = c;
    }
    REP(i, N + 1) REP(j, 1 << M) best[i][j] = -INF;
    best[0][0] = 0;

    FOR(l, 1, N) {
        REP(cfg, 1 << M) if (best[l - 1][cfg] >= 0) {
            REP(cfg2, 1 << M) {
                bool good = true;
                int cnt = 0;
                REP(j, M) if (((1 << j) & cfg2)) {
                    ++cnt;
                    if (mat[l][j] == 'x')
                        { good = false; break; }
                    if (j > 0 && (((1 << (j - 1) & cfg2)) || ((1 << (j - 1) & cfg))))
                        { good = false; break; }
                    if (j < M - 1 && (((1 << (j + 1) & cfg2)) || ((1 << (j + 1) & cfg))))
                        { good = false; break; }
                }
                if (good == false) continue;
                if (best[l][cfg2] < best[l - 1][cfg] + cnt) {
                    best[l][cfg2] = best[l - 1][cfg] + cnt;
                }
                if (best[l][cfg2] > sol) sol = best[l][cfg2];
            }
        }
    }
    printf("%d\n", sol);
}

int main(int argc, char **argv) {
    assert(argc > 1);
    string file_in = string(argv[1]) + ".in";
    string file_out = string(argv[1]) + ".out";
    freopen(file_in.c_str(), "rt", stdin);
    freopen(file_out.c_str(), "wt", stdout);
    int nrt, nrc;

    for (scanf("%d", &nrt), nrc = 1; nrc <= nrt; ++nrc) {
        TIP(nrc);
        printf("Case #%d: ", nrc);
        solve_case();
        fflush(stdout);
    }

    fclose(stdin);
    fclose(stdout);
    cerr << "DONE!\n";
    return 0;
}

