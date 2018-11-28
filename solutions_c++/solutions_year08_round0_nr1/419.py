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

#define FILE_NAME "A-large"

map<string, int> seid;
char name[256];
int N, Q;

int main() {
    freopen(FILE_NAME".in", "rt", stdin);
    freopen(FILE_NAME".out", "wt", stdout);

    int nr_t, nr_c;
    for (scanf("%d\n", &nr_t), nr_c = 1; nr_c <= nr_t; ++nr_c) {

        // Clear data structures.
        seid.clear();

        scanf("%d\n", &N);
        REP(i, N) {
            fgets(name, 256, stdin);
            int len = strlen(name);
            while (name[len - 1] == '\n') {
                name[--len] = 0;
            }
            seid[name] = i;
        }

        vector<int> seq;
        scanf("%d\n", &Q);
        seq.reserve(Q);
        REP(i, Q) {
            fgets(name, 256, stdin);
            int len = strlen(name);
            while (name[len - 1] == '\n') {
                name[--len] = 0;
            }
            map<string, int> :: iterator it = seid.find(name);
//            fprintf(stderr, "name = %s\n", name);
            assert(it != seid.end());
            seq.push_back(it->second);
        }

        vector<int> viz(N, 0);
        int nx = N, sol = 0;

        REP(i, seq.sz) {
            if (viz[seq[i]] == 0) {
                if (nx == 1) {
                    REP(j, viz.sz) viz[j] = 0;
                    ++sol;
                    nx = N;
                }
                viz[seq[i]] = 1;
                --nx;
            }
        }
        printf("Case #%d: %d\n", nr_c, sol);
    }

    fclose(stdin);
    fclose(stdout);
    return 0;
}

