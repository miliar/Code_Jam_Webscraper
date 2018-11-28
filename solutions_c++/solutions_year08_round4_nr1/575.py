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

const int MAXN = 16 * 1024;

int cache[2][MAXN];

#define left(x) ( 2 * (x) + 1)
#define right(x) ( 2 * (x) + 2)

int M;
int V[MAXN], G[MAXN], C[MAXN];

int fun(int nod, int gv) {
    if (nod >= M) return INF;
    if (cache[gv][nod] != -1) return cache[gv][nod];
    if (V[nod] == gv) {
        return cache[gv][nod] = 0;
    }
    int ret = INF;
    if (gv) {
        if (G[nod]) {
            ret = min(ret, fun(2 * nod + 1, 1) + fun(2 * nod + 2, 1));
        } else {
            ret = min(ret, min(fun(2 * nod + 1, 1), fun(right(nod), 1)));
        }

        if (C[nod]) {
            if (G[nod]) {
                ret = min(ret, min(fun(2 * nod + 1, 1), fun(right(nod), 1)) + 1);
            } else {
                ret = min(ret, fun(2 * nod + 1, 1) + fun(2 * nod + 2, 1) + 1);
            }
        }
    } else {
        if (G[nod] == 0) {
            ret = min(ret, fun(2 * nod + 1, 0) + fun(2 * nod + 2, 0));
        } else {
            ret = min(ret, min(fun(2 * nod + 1, 0), fun(right(nod), 0)));
        }

        if (C[nod]) {
            if (G[nod] == 0) {
                ret = min(ret, min(fun(2 * nod + 1, 0), fun(right(nod), 0)) + 1);
            } else {
                ret = min(ret, fun(2 * nod + 1, 0) + fun(2 * nod + 2, 0) + 1);
            }
        }
    }
    return cache[gv][nod] = ret;
}

int main(int argc, char **argv) {
    assert(argc > 1);
    string file_in = string(argv[1]) + ".in";
    string file_out = string(argv[1]) + ".out";
    freopen(file_in.c_str(), "rt", stdin);
    freopen(file_out.c_str(), "wt", stdout);
    int nrt, nrc, GV;

    for (scanf("%d", &nrt), nrc = 1; nrc <= nrt; ++nrc) {
        TIP(nrc);
        scanf("%d %d", &M, &GV);
        REP(i, M) cache[0][i] = cache[1][i] = -1;
        REP(i, M / 2) scanf("%d %d", G + i, C + i);
        FOR(i, M / 2, M - 1) scanf("%d", V + i);
        for (int i = M / 2 - 1; i >= 0; --i) {
            if (G[i]) V[i] = V[2 * i + 1] && V[2 * i + 2];
            else V[i] = V[2 * i + 1] || V[2 * i + 2];
        }
        int sol = INF;
        TIP(V[0], GV);
        sol = fun(0, GV);
        if (sol <= MAXN) {
            printf("Case #%d: %d\n", nrc, sol);
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

