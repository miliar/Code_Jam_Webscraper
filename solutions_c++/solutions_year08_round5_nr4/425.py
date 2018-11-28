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

const int MOD = 10007;
int N, M, R;
int rn[16], rm[16];

int nrbits(int x) {
    int ret = 0;
    for (; x; x /= 2) if (x % 2) ++ret;
    return ret;
}

int product(int a, int b) {
    int ret = 1;
    for (int i = a; i <= b; ++i) {
        int x = i;
        for (; x % MOD == 0; x /= MOD)
            ;
        ret = ((LL) ret * x) % MOD;
    }
    return ret;
}

int power(int a, int p) {
    if (p == 0) return 1;
    if (p == 1) return a % MOD;
    if (p % 2) return (a * power(a, p - 1)) % MOD;
    int temp = power(a, p / 2);
    return (temp * temp) % MOD;
}

int inverse(int a) {
    if (a > MOD) a %= MOD;
    return power(a, MOD - 2);
}

int comb(int n, int k) {
    //TIP(n, k);
    int ret = 1, cnt = 0;
    for (int i = (((n - k + 1) + MOD - 1) / MOD) * MOD; i <= n; i += MOD) {
        for (int x = i; x % MOD == 0; x /= MOD)
            ++cnt;
    }
    for (int i = MOD; i <= k; i += MOD) {
        for (int x = i; x % MOD == 0; x /= MOD)
            --cnt;
    }
    assert(cnt >= 0);
    if (cnt > 0) {
        return 0;
    }
    ret = product(n - k + 1, n) * inverse(product(1, k));
    ret %= MOD;
    return ret;
}

int solve(int h, int w) {
    assert(h >= 0);
    assert(w >= 0);
    if (h == 0 && w == 0) return 1;
    int x = 2 * h - w, y = 2 * w - h;
    if (x < 0 || y < 0 || x % 3 || y % 3) return 0;
    x /= 3, y /= 3;
    return comb(x + y, min(x, y));
}

int count(int cfg) {
    vector<pair<int, int> > T;
    T.PB(MP(0, 0));
    T.PB(MP(N, M));

    REP(i, R) {
        if ((1 << i) & cfg) {
            T.PB(MP(rn[i], rm[i]));
        }
    }
    sort(ALL(T));
    REP(i, SZ(T) - 1) if (T[i].second > T[i + 1].second) return 0;

    int ret = 1;
    REP(i, SZ(T) - 1) {
        ret = (ret * solve(T[i + 1].first - T[i].first, T[i + 1].second - T[i].second)) % MOD;
        if (ret == 0) return 0;
    }
    return ret;
}

void solve_case() {
    scanf("%d %d %d", &N, &M, &R);
    --N, --M;
    REP(i, R) scanf("%d %d", rn + i, rm + i), rn[i]--, rm[i]--;

    int sol = 0;
    REP(i, 1 << R) {
        if (nrbits(i) % 2) {
            sol = (sol - count(i) + MOD) % MOD;
        } else {
            sol = (sol + count(i)) % MOD;
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

