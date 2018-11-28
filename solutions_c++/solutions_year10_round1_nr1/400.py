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

char mat[55][55];
bool red, blue;

void work(int k, int n) {
    for( int i = 0; i < n; ++i ) {
		for( int j = 0; j < n; ++j ) {
			char now = mat[i][j];
			if( now == '.' )    continue;
			int p;
			if( j+k-1 < n ) {
				for( p = 1; p < k; ++p )
					if( mat[i][p+j] != now )    break;
				if( p == k ) {
					if( now == 'R' )    red = 1;
					if( now == 'B' )    blue = 1;
				}
			}
			if( i+k-1 < n ) {
			    for( p = 1; p < k; ++p )
					if( mat[i+p][j] != now )    break;
				if( p == k ) {
					if( now == 'R' )    red = 1;
					if( now == 'B' )    blue = 1;
				}
			}
			if( j+k-1 < n && i-(k-1) >= 0 ) {
				for( p = 1; p < k; ++p )
					if( mat[i-p][j+p] != now )    break;
				if( p == k ) {
					if( now == 'R' )    red = 1;
					if( now == 'B' )    blue = 1;
				}
			}
			if( j+k-1 < n && i+(k-1) < n ) {
				for( p = 1; p < k; ++p )
					if( mat[i+p][j+p] != now )    break;
				if( p == k ) {
					if( now == 'R' )    red = 1;
					if( now == 'B' )    blue = 1;
				}
			}
		}
	}
}

int main()
{
	freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
	int T;
	cin >> T;
	int cnd = 0;
	int n, k;
	while( T-- ) {
		cin >> n >> k;
        for( int i =  0; i < n; ++i )
			scanf("%s", mat[i]);
		for( int i = 0; i < n; ++i ) {
			for( int j = n-2; j >= 0; --j ) {
				int t = j;
				if( mat[i][t] != '.' ) {
					while( t+1 < n && mat[i][t+1] == '.' ) {
					    mat[i][t+1] = mat[i][t];
						mat[i][t] = '.';
						t++;
					}
				}
			}
		}
        red = 0, blue = 0;
        work(k, n);
		printf("Case #%d: ", ++cnd);
		if( red && blue )    puts("Both");
		else if( red )    puts("Red");
		else if( blue )    puts("Blue");
		else puts("Neither");
	}
	return 0;
}