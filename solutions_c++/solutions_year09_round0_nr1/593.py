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

int main()
{
	freopen("1.txt", "w", stdout);
	int len, n, m;
	string s[5005], flag[5005];
	while ( cin >> len >> n >> m ) {
	    for ( int i = 0; i < n; ++i )
			cin >> s[i];
		for ( int k = 1; k <= m; ++k ) {
		    string str, t[505];
			cin >> str;
			int cnd = 0, flag = 0;
			for ( int i = 0; i < str.size(); ++i ) {
			    if ( str[i] == '(' )    flag = 1;
				else if ( flag && str[i] != '(' && str[i] != ')' ) {
				    t[cnd] += str[i];
				}
				else if ( flag == 0 && str[i] != '(' && str[i] != ')' ) {
				    t[cnd] += str[i];
					cnd++;
				}
				else if ( str[i] == ')' ) {
					flag = 0;
				    cnd++;
				}
			}
			int ans = 0, i1, j1, f;
			if ( cnd != len )    goto a1;
            //for ( int i = 0; i < cnd; ++i )
			//	cout << t[i] << endl;
			for ( i1 = 0; i1 < n; ++i1 ) {
				for ( j1 = 0; j1 < len; ++j1 ) {
					f = 0;
					for ( int k1 = 0; k1 < t[j1].size(); ++k1 )
						if ( t[j1][k1] == s[i1][j1] ) {f = 1; break;}
					if ( f == 0 )    break;
				}
				if ( j1 == len )    ans++;
			}
			printf("Case #%d: %d\n", k, ans);
			continue;
			a1: printf("Case #%d: 0\n", k);
		}
	}
	return 0;
}
