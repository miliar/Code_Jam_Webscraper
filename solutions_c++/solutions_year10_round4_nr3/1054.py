#include <cstdlib>
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

int mat[105][105];

int main()
{
	freopen("C-small-attempt0(2).in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
	int T;
	cin >> T;
	int cnd = 0;
	while( T-- ) {
		int n, r1, r2, c1, c2;
		cin >> n;
		mset(mat, 0);
		int now = 0;
		for( int i = 0; i < n; ++i ) {
			cin >> r1 >> c1 >> r2 >> c2;

			for( int j = r1; j <= r2; ++j ) {
				for( int k = c1; k <= c2; ++k ) {
					mat[j][k] = 1;
				}
			}
		}
		for( int i = 0; i <= 100; ++i )
			for( int j = 0; j <= 100; ++j )
				if( mat[i][j] == 1 )    now++;

		int ans = 0;
		int mat1[105][105];
		while( now != 0 ) {
			ans++;
			mset(mat1, 0);
			for( int i = 1; i <= 100; ++i ) {
				for( int j = 1; j <= 100; ++j ) {
					mat1[i][j] = mat[i][j];
					if( mat[i][j] == 1 && mat[i-1][j] == 0 && mat[i][j-1] == 0 ) {
						mat1[i][j] = 0;
					}
					if( mat[i][j] == 0 && mat[i-1][j] == 1 && mat[i][j-1] == 1 ) {
						mat1[i][j] = 1;
					}
				}
			}
			now = 0;
            for( int i = 0; i <= 100; ++i ) {
				for( int j = 0; j <= 100; ++j ) {
				    mat[i][j] = mat1[i][j];
					if( mat[i][j] == 1 )    now++;
				}
			}
		}
		printf("Case #%d: %d\n", ++cnd, ans);
	}
	return 0;
}
