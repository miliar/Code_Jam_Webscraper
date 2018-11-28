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
#define sz size()
#define pb push_back

#define FORD(i, N, M) for (int i = (int)(N); i >= (int)(M); --i)
#define FORI(it, x) for (__typeof((x).begin()) it = (x).begin(); it != (x).end(); ++it)
#define mp make_pair
#define INF 0x3f3f3f3f
typedef long long LL;

#define FILE_NAME "b-large"

int main() {
    freopen(FILE_NAME".in", "rt", stdin);
    freopen(FILE_NAME".out", "wt", stdout);
    int nrt, nrc, T, NA, NB, h1, m1, h2, m2;

    for (scanf("%d", &nrt), nrc = 1; nrc <= nrt; ++nrc) {
        scanf("%d", &T);
        scanf("%d %d", &NA, &NB);

        vector<pair<int, int> > va, vb;
        REP(i, NA) {
            scanf("%d:%d %d:%d", &h1, &m1, &h2, &m2);
            va.push_back(mp(h1 * 60 + m1, h2 * 60 + m2));
        }
        REP(i, NB) {
            scanf("%d:%d %d:%d", &h1, &m1, &h2, &m2);
            vb.push_back(mp(h1 * 60 + m1, h2 * 60 + m2));
        }
        sort(ALL(va));
        sort(ALL(vb));

        vector<int> fa(2048, 0), fb(2048, 0);
        int nrA = 0, nrB = 0, solA = 0, solB = 0;
        int pa = 0, pb = 0, tm = 0;

//        TIP(va, vb);
        while (pa < (int) va.sz || pb < (int) vb.sz) {
            assert(tm < (int) fa.sz);
            nrA += fa[tm];
            nrB += fb[tm];

            while (pa < (int) va.sz && va[pa].first == tm) {
                if (nrA == 0) {
                    ++solA;
                } else {
                    --nrA;
                }
                assert(va[pa].second + T < (int) fb.sz);
                ++fb[va[pa].second + T];
                ++pa;
            }
            while (pb < (int) vb.sz && vb[pb].first == tm) {
                if (nrB == 0) {
                    ++solB;
                } else {
                    --nrB;
                }
                assert(vb[pb].second + T < (int) fa.sz);
                ++fa[vb[pb].second + T];
                ++pb;
            }
            ++tm;
        }
        printf("Case #%d: %d %d\n", nrc, solA, solB);
    }

    fclose(stdin);
    fclose(stdout);
    return 0;
}

