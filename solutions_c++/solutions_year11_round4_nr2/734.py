#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <cstring>
#include <cmath>
#include <ctime>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <bitset>
#include <set>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <numeric>
#include <utility>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef stringstream ss;
typedef istringstream iss;

const int INF = (int)2E9;
const ll LINF = (ll)9E18;

const ld PI = acos(-1.0);
const ld EPS = 1E-11;

#define FOR(i, a, b) for (int i = (a); i <= (b); ++i)
#define FORD(i, a, b) for (int i = (a); i >= (b); --i)
#define REP(i, a) for (int i = 0; i < (a); ++i)
#define REPD(i, a) for (int i = (a) - 1; i >= 0; --i)
#define FIT(it, v) for (typeof((v).begin())it = (v).begin(); it != (v).end(); ++it)
#define FITD(it, v) for (typeof((v).rbegin())it = (v).rbegin(); it != (v).rend(); ++it)

#define LET(a, b) typeof(b) a(b)
#define ALL(v) (v).begin(), (v).end()
#define SET(a, x) memset((a), (x), sizeof(a))
#define SIZE(a) ((int)(a).size())

#define EXIST(a, b) (find(ALL(a), (b)) != (a).end())
#define SORT(x) sort(ALL(x))
#define GSORT(x) sort(ALL(x), greater<typeof(*((x).begin()))>())
#define ENUM(v) FIT(it, (v)) cout << *it << " "; cout << endl

#define PB push_back
#define MP make_pair
#define F first
#define S second

template<typename T> inline T sqr(const T x) { return x * x; }
template<typename T> T gcd(T a, T b) { return (b == 0) ? a : gcd(b, a % b); }
template<typename T> T lcm(T a, T b) { return a / gcd(a, b) * b; }
template<typename T> T mod(T a, T b) { a %= b; if (a < 0) a += b; return a; }
template<typename T> inline T rad(const T x) { return x * PI / 180; }

template<typename T> inline string toString(T x) { ostringstream oss; oss << x; return oss.str(); }
inline ll toInt(const string& st) { istringstream iss(st); ll x; iss >> x; return x; }
inline ld toDouble(const string& st) { istringstream iss(st); ld x; iss >> x; return x; }
inline string toLower(string st) { REP(i, SIZE(st)) st[i] = tolower(st[i]); return st; }
inline string toUpper(string st) { REP(i, SIZE(st)) st[i] = toupper(st[i]); return st; }

const int dx[] = {-1, 0, 1, 0}; const int dy[] = {0, -1, 0, 1};

int DEBUG = false;
const char DEBUG_PARAM[] = "__LOCAL_TESTING";

const int MAXCLOCK = 100;
int aClock[MAXCLOCK], mClock[MAXCLOCK], nClock = 0, iClock = 0;
inline void tick(int maxTime = 10000) {
	if (false) {
		mClock[nClock] = maxTime;
		aClock[nClock++] = clock();
	}
}
inline void untick(string name = "Execution Time") {
	if (false) {
		int numClock = clock() - aClock[--nClock];
		cout << "@ " << name << ": [" << (int)((double)(numClock) / CLOCKS_PER_SEC * 1000) << " ms]";
		if (numClock > (int)(mClock[nClock])) cout << " [TLE]";
		else if (numClock > (int)(mClock[nClock] * 0.9)) cout << " [almost TLE]";
		cout << endl;
	}
}

const char IN[] = "_.in";
const char OUT[] = "_.out";

int ntest = 1, test = 1;

/* BEGIN DECLARATION */
const int MAXN = 15;

int r, c, d;
char a[MAXN][MAXN];
/* END DECLARATION */

inline void run() {
	/* BEGIN INITIALIZATION */
	cin >> ntest;
	/* END INITIALIZATION */
	for (test = 1; test <= ntest; ++test) {
		tick((int)2E3);
		/* BEGIN IMPLEMENTATION */
		cin >> r >> c >> d;
		cin.ignore();
		string s;
		FOR(i, 1, r) {
			getline(cin, s);
			FOR(j, 1, c) {
				a[i][j] = s[j - 1] - '0';
			}
		}
		int found = -1;
		int from = min(r, c);
		FORD(k, from, 3) {
			FOR(i, 1, r - k + 1) {
				FOR(j, 1, c - k + 1) {
					ld ci = 2 * i + (k - 1), cj = 2 * j + (k - 1), mi = 0, mj = 0;
					FOR(u, i, i + k - 1) {
						FOR(v, j, j + k - 1) {
							if ((u == i || u == i + k - 1) && (v == j || v == j + k - 1)) {
								continue;
							}
							mi += (2 * u - ci) * a[u][v];
							mj += (2 * v - cj) * a[u][v];
						}
					}
					if (mi == 0 && mj == 0) {
						found = k;
						goto checkFound;
					}
				}
			}
		}
		checkFound: ;
		cout << "Case #" << test << ": ";
		if (found != -1) {
			cout << found << endl;
		} else {
			cout << "IMPOSSIBLE" << endl;
		}
		/* END IMPLEMENTATION */
		untick("#" + toString(test));
	}
}

int main(int argc, char* argv[]) {
	if (argc > 1 && strcmp(argv[1], DEBUG_PARAM) == 0) {
		DEBUG = true;
	}
	if (DEBUG) {
		tick((int)1E4);
		freopen(IN, "r", stdin);
		freopen(OUT, "w", stdout);
	}
	run();
	if (DEBUG) {
		untick("TOTAL");
	}
	return 0;
}
