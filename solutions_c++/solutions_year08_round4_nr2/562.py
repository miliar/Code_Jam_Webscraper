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

const int MAXN  = 10001;

short viz[MAXN * MAXN];

int main(int argc, char **argv) {
    assert(argc > 1);
    string file_in = string(argv[1]) + ".in";
    string file_out = string(argv[1]) + ".out";
    freopen(file_in.c_str(), "rt", stdin);
    freopen(file_out.c_str(), "wt", stdout);
    int nrt, nrc;

    int N, M, A;
    for (scanf("%d", &nrt), nrc = 1; nrc <= nrt; ++nrc) {
        TIP(nrc);
        scanf("%d %d %d", &N, &M, &A);

        int x1 = -1, y1 = -1, x2 = -1, y2 = -1;
        FOR(i, 0, N) FOR(j, 0, M) {
            FOR(k, i, N) FOR(l, 0, M) {
                int area = -1;
                if (l < j) {
                    area = i * j + (k - i) * (j + l) - k * l;
                } else {
                    area = k * l - i * j - (k - i) * (j + l);
                }
                if (area == A) {
                    x1 = i, y1 = j, x2 = k, y2 = l;
                    goto found_sol;
                }
            }
        }
        /*
        FOR(i, 0, N) FOR(j, 0, M) {
            int tmp = i * j;
            if (tmp >= A && viz[tmp - A]) {
                x2 = i, y1 = j;
                x1 = viz[tmp - A];
                if (viz[tmp - A]) {
                    y2 = (tmp - A) / viz[tmp - A];
                } else {
                    y2 = M;
                }
                goto found_sol;
            }
            viz[i * j] = i;
        }*/

found_sol:
        if (x1 != -1) {
            printf("Case #%d: %d %d %d %d %d %d\n", nrc, 0, 0, x1, y1, x2, y2);
        } else {
            printf("Case #%d: IMPOSSIBLE\n", nrc);
        }
        fflush(stdout);
    }

    fclose(stdin);
    fclose(stdout);
    cerr << "DONE!\n";
    return 0;
}

