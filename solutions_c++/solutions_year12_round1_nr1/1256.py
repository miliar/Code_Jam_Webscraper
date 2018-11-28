#include <memory.h>
#include <stdio.h>
#include <assert.h>

#include <string>
#include <map>
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <queue>
#include <cstdio>
#include <ctime>
#include <cmath>
#include <sstream>
#include <iomanip>

using namespace std;

typedef long long int64;
typedef long long ll;
typedef pair<int , int> pii;
typedef pair<ll, ll> pll;
typedef vector<int > vi;
typedef vector<pii> vpii;
typedef vector<ll> vll;

#define ALL(x) (x).begin(), (x).end()
#define CLEAR(x) (x).clear()
#define RESET(x) memset((x), 0, sizeof (x))
#define MP(x, y) make_pair((x), (y))

#define FOR(i, b, e) for (int i = (b); i < (e); ++i)
#define RE(i, n) FOR(i, 0, (n))
#define two(X) (1<<(X))
#define twoL(X) (((int64)(1))<<(X))
#define contain(S,X) (((S)&two(X))>0)
#define containL(S,X) (((S)&twoL(X))>0)
int64 toInt64(string s){int64 r=0;istringstream sin(s);sin>>r;return r;}
int toInt(string s){int r=0;istringstream sin(s);sin>>r;return r;}
string toString(int64 v){ostringstream sout;sout<<v;return sout.str();}
string toString(int v){ostringstream sout;sout<<v;return sout.str();}

template<class T> inline T countbit(T n){return (n==0)?0:(1+countbit(n&(n-1)));}
template<class T> inline T lowbit(T n){return (n^(n-1))&n;}
template<class T> inline T sqr(T x){ return x * x;}
template<class T> inline T gcd(T a,T b){ if(a < 0) return gcd(-a,b); if (b < 0) return gcd(a,-b); return (b == 0)?a:gcd(b,a%b);}
template<class T> inline T lcm(T a,T b){return a*(b/gcd(a,b));}
template<class T> void out(T A[], int n){for(int i = 0;i < n;++i) cout << A[i] << " ";cout << endl;}
template<class T> void out(vector<T> A, int n = -1){if(n==-1) n = A.size();for (int i = 0;i < n;++i) cout << A[i] << " " ;cout << endl;}

const int maxn = 1e5 + 5;
const int INF = 1e10;

void Solve() {
	int n, m;
	scanf("%d %d", &n, &m);
	vector<double> p(n + 1);
	RE(i, n) scanf("%lf", &p[i + 1]);
	vector<double> d(n + 1, 0);
	d[0] = 1;
	for (int i = 1; i <= n; ++i) d[i] = p[i] * d[i - 1];
	double ans = m + 2;
	for (int i = n; i >= 0; --i) {
		int t = n - i;
		int t1 = m - i + 1;
		int t2 = t1 + m + 1;
		double len = (t + t1) * d[i] + (t + t2) * (1 - d[i]);
		if (ans > len)
			ans = len;
	}
	printf("%.7lf\n", ans);
	// cout << ans << endl;
}

int main() {
	// freopen("in.txt", "r", stdin);
	//freopen("A-large.in", "r", stdin);
	//freopen("A-large.out", "w", stdout);
	int ncase;
	cin >> ncase;
	RE(tt, ncase) {
		cout << "Case #" << tt + 1 << ": ";
		Solve();
	}
}