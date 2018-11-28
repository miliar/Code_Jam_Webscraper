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

#define FILE_NAME "b-small"

const int MAXN = 1024 * 1024;

int H[MAXN];
int mul[MAXN];
int viz[MAXN];
map<LL, int> repr;

int get_mul(int i) {
    int r = i;
    while (mul[r] != r) {
        r = mul[r];
    }
    while (mul[i] != r) {
        int tmp = mul[i];
        mul[i] = r;
        i = tmp;
    }
    return r;
}

void join(int i, int j) {
    if (H[i] > H[j]) {
        mul[j] = i;
    } else {
        mul[i] = j;
        H[j] += (H[i] == H[j]);
    }
}

inline void do_the_voodoo(LL div, int ind) {
    if (repr[div] == 0) {
        repr[div] = ind;
    } else {
        join(get_mul(repr[div]), get_mul(ind));
    }
}

int main() {
    freopen(FILE_NAME".in", "rt", stdin);
    freopen(FILE_NAME".out", "wt", stdout);
    int nrt, nrc;
    LL A, B, P;

    for (scanf("%d", &nrt), nrc = 1; nrc <= nrt; ++nrc) {
        scanf("%lld %lld %lld", &A, &B, &P);
        CLEAR(H);
        repr.clear();
        FOR(i, A, B) {
            mul[i - A + 1] = i - A + 1;
        }
        FOR(i, A, B) {
            LL x = i;
            for (LL p = 2; p * p <= x; ++p) {
                if (x % p == 0) {
                    while (x % p == 0) x /= p;
                    if (p >= P) {
                        do_the_voodoo(p, i - A + 1);
                    }
                }
            }
            if (x > 1) {
                if (x >= P) {
                    do_the_voodoo(x, i - A + 1);
                }
            }
        }
        CLEAR(viz);
        int sol = 0;
        FOR(i, 1, B - A + 1) {
            sol += 1 - viz[get_mul(i)];
            viz[get_mul(i)] = 1;
        }
        printf("Case #%d: %d\n", nrc, sol);
    }

    fclose(stdin);
    fclose(stdout);
    return 0;
}

