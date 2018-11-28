#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <algorithm>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <vector>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef vector<int> vi;
typedef vector<string> vs;

const int INF = (int) 1E9;
const ll LINF = (ll) 1E18;

#define FOR(i, a, b) for (int i = (a); i <= (b); i++)
#define FORD(i, a, b) for (int i = (a); i >= (b); i--)
#define REP(i, a) for (int i = 0; i < (a); i++)
#define REPD(i, a) for (int i = (a) - 1; i >= 0; i--)
#define FIT(it, v) for (typeof((v).begin())it = (v).begin(); it != (v).end(); ++it)
#define FITD(it, v) for (typeof((v).rbegin())it = (v).rbegin(); it != (v).rend(); ++it)

#define ALL(v) (v).begin(), (v).end()
#define SET(a, x) memset((a), (x), sizeof(a))
#define SIZE(a) ((int)(a).size())

#define SORT(x) sort(ALL(x))
#define GSORT(x) sort(ALL(x), greater<typeof(*((x).begin()))>())
#define UNIQUE(v) SORT(v); (v).resize(unique(ALL(v)) - (v).begin())

#define PB push_back
#define MP make_pair
#define F first
#define S second

int INP, AM;
#define BUFSIZE (1<<10)
char BUF[BUFSIZE + 1], *inp = BUF;
#define GETCHAR(INP) { \
    if(!*inp) { \
        fread(BUF,1,BUFSIZE,stdin); \
        inp=BUF; \
    } \
    INP=*inp++; \
}
#define DIG(a) (((a)>='0')&&((a)<='9'))
#define GN(j) { \
    AM=0;\
    GETCHAR(INP); while(!DIG(INP) && INP!='-') GETCHAR(INP);\
    if (INP=='-') {AM=1;GETCHAR(INP);} \
    j=INP-'0'; GETCHAR(INP); \
    while(DIG(INP)){j=10*j+(INP-'0');GETCHAR(INP);} \
    if (AM) j=-j;\
}

template<typename T> T gcd(T a, T b) {
	return (b == 0) ? abs(a) : gcd(b, a % b);
}
template<typename T> inline T lcm(T a, T b) {
	return a / gcd(a, b) * b;
}
template<typename T> inline T sqr(T x) {
	return x * x;
}

const char DEBUG_PARAM[] = "__LOCAL_TESTING";

const char IN[] = "input.txt";
const char OUT[] = "output.txt";

int ntest = 0, test;

inline void init();
inline void run();
inline void stop() {
	ntest = test - 1;
}

int main(int argc, char* argv[]) {
	if (argc > 1 && strcmp(argv[1], DEBUG_PARAM) == 0) {
		freopen(IN, "r", stdin);
		//		freopen(OUT, "w", stdout);
	}
	init();
	if (ntest == 0) {
		puts("ntest = ?");
		return 0;
	}
	for (test = 1; test <= ntest; test++) {
		run();
	}
	return 0;
}

/* IMPLEMENTATION */

const int dx[] = { -1, 0, 0, 1 };
const int dy[] = { 0, -1, 1, 0 };

const ld EPS = 1E-9;
const ll MODULO = 1000000007LL;
string ss[3000 + 5];
inline void init() {
	ntest = 1; // Input ntest
	cin >> ntest;
	stringstream s;
	FOR(i,1,3000)
		s << i << " ";
	FOR(i,1,3000)
		s >> ss[i];
}
const int maxn = 100 + 5;
int a, b;

inline bool ok(string a, string b) {
	if (SIZE(a) != SIZE(b))
		return false;
	FOR(i,1,SIZE(a) -1) {
		if (b == a.substr(i, SIZE(a) - i) + a.substr(0, i))
			return true;
	}
	return false;
}
void solve() {
	int res = 0;
	FOR(i,a,b)
		FOR(j,i+1,b) {
			if (ok(ss[i], ss[j]))
				res++;
		}
	cout << "Case #" << test << ": " << res << endl;
}
inline void run() {
	cin >> a >> b;
	solve();
}
