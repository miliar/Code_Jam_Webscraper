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

#define FILE_NAME "A-large"


int main() {
    freopen(FILE_NAME".in", "rt", stdin);
    freopen(FILE_NAME".out", "wt", stdout);
    int nrt, nrc;
    LL n, C, D, A, B, M, X, Y;

    for (scanf("%d", &nrt), nrc = 1; nrc <= nrt; ++nrc) {
        TIP(nrc);
        vector<LL> T(9, 0);
        scanf("%lld %lld %lld %lld %lld %lld %lld %lld",
                &n, &A, &B, &C, &D, &X, &Y, &M);
        T[(X % 3) * 3 + Y % 3]++;
        FOR(i, 1, n - 1) {
            X = (A * X + B) % M;
            Y = (C * Y + D) % M;
            T[(X % 3) * 3 + Y % 3]++;
        }

        LL sol = 0;
        REP(i, 9) FOR(j, i, 8) FOR(k, j, 8) {
            if ((i % 3 + j % 3 + k % 3) % 3 ||
                (i / 3 + j / 3 + k / 3) % 3) continue;
            if (i == j) {
                if (j == k) {
                    sol += T[i] * (T[j] - 1) * (T[k] - 2) / 6;
                } else {
                    sol += T[i] * (T[j] - 1) * T[k] / 2;
                }
            } else {
                if (j == k) {
                    sol += T[i] * T[j] * (T[k] - 1) / 2;
                } else {
                    sol += T[i] * T[j] * T[k];
                }
            }
        }
        printf("Case #%d: %lld\n", nrc, sol);
    }

    fclose(stdin);
    fclose(stdout);
    return 0;
}

