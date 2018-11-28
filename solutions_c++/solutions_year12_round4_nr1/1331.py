#pragma comment(linker, "/STACK:66777216")
#define _USE_MATH_DEFINES
#define _CRT_SECURE_NO_WARNINGS
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <assert.h>
#include <memory.h>
#pragma hdrstop

using namespace std;

#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define y0 __MY_Y0__
#define y1 __MY_Y1__
#define sz(a) (int)a.size()
#define fill(a, x) memset (a, x, sizeof(a))

#ifdef _DEBUG
	#define Eo(x) {cout << "# " << #x << " = " << (x) << endl;}
	#define E(x) {cout << "# " << #x << " = " << (x) << " ";}
	#define Ou(x) {cout << "# " << (x) << endl;}
	#define OK {cout << "# OK    Line : " << __LINE__ << endl;}
#else
	#define Eo(x)
	#define E(x)
	#define Ou(x)
	#define OK
#endif

#ifdef WIN32
	#define LLD "%I64d"
#else
	#define LLD "%lld"
#endif

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;

inline void sIO() {
#ifdef _DEBUG
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
#endif
}
inline void iIO() {freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);}
inline void fIO(string fn) {
#ifdef _DEBUG
	freopen("input.txt", "r", stdin); freopen ("output.txt", "w", stdout);
#else
	freopen((fn + ".in").c_str(), "r", stdin); freopen((fn + ".out").c_str(), "w", stdout);
#endif
}
inline void TM() {
#ifdef _DEBUG
	cout << endl << "# Time: " << clock() / 1000. << endl;
#endif
}
template<class T> inline T abs(T x) {return x < 0 ? -x : x;}
template<class T> inline T sqr(T x) {return x * x;}
template<class T> inline T gcd(T a, T b) {if (a < b) swap(a, b); while (b) {a %= b; swap(a, b);} return a;}
template<class T> inline T lcm(T a, T b) {return a * b / gcd(a, b);}
template<class T> inline bool isPrime(T n) {if (n < 2) return false; T kk = (T)sqrt(n + 0.); for (T i = 2; i <= kk; ++i) if (!(n % i)) return false; return true;}
template<class T> inline string toa(T x) {stringstream ss; ss << x; string ret; ss >> ret; return ret;}
template<class T> inline T ppow(T a, ll b) {T ret = 1; while (b) {if (b & 1) ret *= a; a *= a; b >>= 1;} return ret;}
inline int toi(string s) {stringstream ss; ss << s; int ret; ss >> ret; return ret;}
inline ll tol(string s) {stringstream ss; ss << s; ll ret; ss >> ret; return ret;}
inline void swap(short& a, short& b) {b ^= a ^= b ^= a;}
inline void swap(int& a, int& b) {b ^= a ^= b ^= a;}
inline void swap(char& a, char& b) {b ^= a ^= b ^= a;}
inline void swap(ll& a, ll& b) {b ^= a ^= b ^= a;}
inline char upperCase(char ch) {return (ch >= 'a' && ch <= 'z') ? ch^32 : ch;}
inline char lowerCase(char ch) {return (ch >= 'A' && ch <= 'Z') ? ch^32 : ch;}
inline string upperCase(string s) {int ls = s.length(); for (int i = 0; i < ls; ++i) if (s[i] >= 'a' && s[i] <= 'z') s[i] ^= 32; return s;}
inline string lowerCase(string s) {int ls = s.length(); for (int i = 0; i < ls; ++i) if (s[i] >= 'A' && s[i] <= 'Z') s[i] ^= 32; return s;}
inline int dig(char ch) {return ch - 48;}
inline bool isAlpha(char ch) {return (ch >= 'A' && ch <= 'Z' || ch >= 'a' && ch <= 'z');}
inline bool isDigit(char ch) {return (ch >= '0' && ch <= '9');}
inline bool isLowerCase(char ch) {return (ch >= 'a' && ch <= 'z');}
inline bool isUpperCase(char ch) {return (ch >= 'A' && ch <= 'Z');}

const int INF = 0x3f3f3f3f;
const ll LINF = 0x3f3f3f3f3f3f3f3fLL;
const double EPS = 1e-9;
const int MD = 1000000007;

int __;

int n, a[11111][2], dd, q[11111111][2], h, t, x, y, tt;
bool ok;

int main() {
	sIO();
	scanf("%d", &__);
	for (int _ = 1; _ <= __; ++_) {
		printf("Case #%d: ", _);
		scanf("%d", &n);
		for (int i = 0; i < n; ++i)
			scanf("%d %d", &a[i][0], &a[i][1]);
		scanf("%d", &dd);
		ok = false;
		q[0][0] = 0;
		q[0][1] = a[0][0];
		h = 0;
		t = 0;
		while (h <= t) {
			x = q[h][0];
			y = q[h++][1];
			if (a[x][0] + y >= dd) {
				ok = true;
				break;
			}
			int i = x++;
			while (x < n) {
				tt = a[i][0] + y - a[x][0];
				if (tt < 0) break;
				q[++t][0] = x;
				q[t][1] = min(a[x][0] - a[i][0], a[x][1]);
				x++;
			}
		}
		if (ok) printf("YES"); else printf("NO");
		printf("\n");
	}
	return 0;
}