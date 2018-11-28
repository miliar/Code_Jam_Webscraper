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

char S[1024];
char T[1024];

int main(int argc, char **argv) {
    assert(argc > 1);
    string file_in = string(argv[1]) + ".in";
    string file_out = string(argv[1]) + ".out";
    freopen(file_in.c_str(), "rt", stdin);
    freopen(file_out.c_str(), "wt", stdout);
    int nrt, nrc;

    int k;
    for (scanf("%d\n", &nrt), nrc = 1; nrc <= nrt; ++nrc) {
        TIP(nrc);
        scanf("%d\n%s\n", &k, S);
        vector<int> P;
        REP(i, k) P.PB(i);
        int len = strlen(S);
        int sol = len;
        do {
            for (int i = 0; i < len; i += k) {
                REP(j, k) T[i + j] = S[i + P[j]];
            }
            int tmp = 1;
            FOR(i, 1, len - 1) if (T[i] != T[i - 1]) {
                tmp++;
            }
            if (sol > tmp) sol = tmp;
        } while (next_permutation(ALL(P)));
        printf("Case #%d: %d\n", nrc, sol);
        fflush(stdout);
    }

    fclose(stdin);
    fclose(stdout);
    cerr << "DONE!\n";
    return 0;
}

