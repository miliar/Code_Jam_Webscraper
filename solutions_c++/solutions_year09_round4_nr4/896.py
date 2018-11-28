#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
#include <climits>
#include <ctime>
#include <cfloat>
#include <cassert>
#include <set>
#include <map>
#include <list>
#include <queue>
#include <stack>
#include <deque>
#include <vector>
#include <bitset>
#include <string>
#include <complex>
#include <utility>
#include <sstream>
#include <iomanip>
#include <numeric>
#include <iostream>
#include <valarray>
#include <algorithm>
#include <functional>
using namespace std;

typedef int i32;
typedef unsigned int u32;
typedef long long i64;
typedef unsigned long long u64;

#define two(i)		(1<<(i))
#define twoL(i)		(1LL<<(i))
#define CLR(a,v)	memset(a,v,sizeof(a))
#define MP(a,b)		make_pair(a,b)
#define SIZE(a)		((int)a.size())
#define LENGTH(a)	((int)a.length())
#define REP(i,n)	for(int i=0; i<(n); ++i)
#define REPD(i,n)	for(int i=(n)-1; i>=0; --i)
#define FOR(i,s,e)	for(int i=(s); i<=(e); ++i)
#define FORD(i,s,e)	for(int i=(s); i>=(e); --i)

template<class T>inline int cMin(T& a, T b) {return b<a ? a=b,1:0;}
template<class T>inline int cMax(T& a, T b) {return a<b ? a=b,1:0;}
template<class T>inline T   sqr(T v) {return v*v;}
template<class T>inline T   iabs(T v) {return v<0?-v:v;}
template<class T>inline T   lowBit(T n) {return n&(n^(n-1));}
template<class T>inline int cntBit(T n) {int c=0;for(;n;n&=n-1)++c;return c;}
template<class T>inline string to_str(T v) {ostringstream os; os<<v; return os.str();}

const double  pi = acos(-1.0);
const double  eps = 1e-6;

template<class T>inline int sgn(T v) {return iabs(v)<eps?0:(v<0?-1:1);}
template<class T>inline T gcd(T a, T b)
	{if(a<b) {a^=b;b^=a;a^=b;} while(b) {a%=b;a^=b;b^=a;a^=b;}return a;}
template<class T>inline T lcm(T a, T b) {return a/gcd(a,b)*b;}
/*Given a and b, compute gcd(a,b) = ax + by*/
template<typename T>
T  exgcd(T a, T b, T &x, T &y){
	if(a < 0) {
		T  d = exgcd(b, a, y, x);
		x = -x;  return  d;
    }
	if(b == 0) {x=1; y=0; return a;}
	T  d = exgcd(b, a%b, y, x);
	y -= (a/b)*x;
	return  d;
}

template<class T>inline T mod_inverse(T a, T n)
	{T x,y; exgcd(a,n,x,y); return (x%n+n)%n;}

inline int isPrime(int n) {int i;
	if(n==2)return 1; if(n<2 || !(n&1))return 0;
	for(i=3;i*i<=n;i+=2)if(n%i==0)return 0;return 1;}


char *input_file = "E:/google/CodeJam/CodeJam/D-small-attempt0.in";
char *output_file = "E:/google/CodeJam/CodeJam/D-small-attempt0.out";
const bool zzzz = true;

const int NN = 42;

int  N, x[NN], y[NN], r[NN];

double dis(int i, int j) {return sqrt((x[i]-x[j])*1.0*(x[i]-x[j])
									  + (y[i]-y[j])*1.0*(y[i]-y[j]));}

double solve() {
	int  N;
	scanf("%d", &N);
	REP(i, N) scanf("%d%d%d", x+i, y+i, r+i);
	if(N == 1) return r[0];
	if(N == 2) return max(r[0], r[1]);
	//if(N == 3) {
		double ans = max((dis(0,1)+r[0]+r[1])/2.0, r[2]+0.0);
		ans = min(ans, max((dis(0,2)+r[0]+r[2])/2.0, r[1]+0.0));
		ans = min(ans, max((dis(2,1)+r[2]+r[1])/2.0, r[0]+0.0));
		return ans;
	//}
}

int main() {
	if(zzzz) {freopen(input_file, "r", stdin);freopen(output_file, "w", stdout);}
	int  T;
	scanf("%d", &T);
	FOR(Ti, 1, T) {
		double ans = solve();
		printf("Case #%d: %.8lf\n", Ti, ans);
	}

	return 0;
}

