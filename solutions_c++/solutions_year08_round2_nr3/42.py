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

#define FILE_NAME "C-large"

const int MAXN = 1024 * 1024;
int A[MAXN];
int AIB[MAXN];

inline int LSB(int x) {
    return x & (x - 1) ^ x;
}

int get(int p) {
    if (p <= 0) return 0;
    int ret = 0;
    while (p > 0) {
        ret += AIB[p];
        p -= LSB(p);
    }
    return ret;
}

int get(int l, int r) {
    if (r < l) return 0;
    return get(r) - get(l - 1);
}

void upd(int p, int x) {
    for (int i = p; i < MAXN; i += LSB(i)) {
        AIB[i] += x;
    }
}

int main() {
    freopen(FILE_NAME".in", "rt", stdin);
    freopen(FILE_NAME".out", "wt", stdout);
    int nrt, nrc;
    int K, n, d;

    for (scanf("%d", &nrt), nrc = 1; nrc <= nrt; ++nrc) {
        scanf("%d\n", &K);
        int no_free = K;
        int crt_pos = 0;
        CLEAR(A);
        CLEAR(AIB);

        TIP(nrt, K);
        FOR(i, 1, K) upd(i, 1);
        REP(i, K) {
            int jmp = i % no_free + 1;
            /*
            for (; A[crt_pos] != 0 || jmp > 0; crt_pos = (crt_pos + 1) % K) {
                if (A[crt_pos] == 0) --jmp;
            }
            */
            int start, end;
            int tmp = get(crt_pos + 1, K);
            if (tmp >= jmp) {
                start = crt_pos, end = K - 1;
            } else {
                start = 0, end = crt_pos - 1;
                jmp -= tmp;
            }
            for (; start <= end;) {
                int mid = (start + end) / 2;
                int tmp = get(start + 1, mid + 1);
                if (jmp > tmp) {
                    start = mid + 1;
                    jmp -= tmp;
                } else {
                    end = mid - 1;
                }
            }
            crt_pos = start;
            A[crt_pos] = i + 1;
            upd(crt_pos + 1, -1);
            --no_free;
        }
        printf("Case #%d:", nrc);
        scanf("%d", &n);
        REP(i, n) {
            scanf("%d", &d);
            printf(" %d", A[d - 1]);
        }
        printf("\n");
    }

    fclose(stdin);
    fclose(stdout);
    return 0;
}

