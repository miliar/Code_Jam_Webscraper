#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <ctime>
#include <utility>
#include <stdexcept>

using namespace std;

#define inf (1<<30)
#define PB push_back
#define mset(x,a) memset(x,(a),sizeof(x))
#define SIZE(X) ((int)X.size())
#define dbg(x) cerr<<#x<<" : "<<x<<endl
#define rg(x,y) (x=x>y?x:y)
typedef vector<int> VI;
typedef vector<char> VC;
typedef vector<string> VS;
typedef long long LL;
typedef unsigned long long uLL;
#define twoL(X) (((LL)(1))<<(X))
const double PI=acos(-1.0);
const double eps=1e-11;
template <class T> T sqr(T x) {return x*x;}
template <class T> T gcd(T a, T b) {if(a<0) return (gcd(-a,b)); if(b<0) return (gcd(a,-b)); return (b==0)?a:gcd(b,a%b);}
template <class T> T lcm(T a, T b) {return a*b/gcd(a,b);}
LL toLL(string s) { istringstream sin(s); LL t; sin>>t; return t;}
int toInt(string s) {istringstream sin(s); int t; sin>>t; return t;}
string toString(LL v) {ostringstream sout; sout<<v; return sout.str();}
string toString(int v) {ostringstream sout; sout<<v; return sout.str();}
#define FOREACH(it, a) for(typeof((a).begin()) it = (a).begin(); it!=(a).end(); ++it)
#define ALL(x) ((x).begin(), (x).end())
#define cross(a, b, c)  ((c).x-(a).x)*((b).y-(a).y)-((b).x-(a).x)*((c).y-(a).y)
#define sq_dist(p, q) ((p).x-(q).x)*((p).x-(q).x)+((p).y-(q).y)*((p).y-(q).y)
#define FF(i,n) for(int i = 0; i < n; ++i)

int win(int a, int b) {
    if ( a > b )    swap(a, b);
	if( a == b )    return 0;
	if ( b % a == 0 )    return 1;
	else {
	    if ( win(b % a, a) && b / a == 1 )
			return 0;
		else return 1;
	}
}


int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small.out", "w", stdout);
	int T;
	int a1, a2, b1, b2;
	cin >> T;
	int cnd = 0;
	while( T-- ) {
		cin >> a1 >> a2 >> b1 >> b2;
		int ans = 0;
		for( int i = a1; i <= a2; ++i ) {
			for( int j = b1; j <= b2; ++j ) {
				if( win(i,j) )    ans++;
			}
		}
		printf("Case #%d: %d\n", ++cnd, ans);
	}
	return 0;
}


