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
	int T;
	string s;
	cin >> T;
	int cnt = 0;
	while ( T-- ) {
	    cin >> s;
		if ( s.size() == 1 )  {
		    printf("Case #%d: ", ++cnt);
		    cout << "1" << endl;
		    continue;
		}  
		string str;
		str = s;
		int num = 1;
		sort(str.begin(), str.end());
		for ( int i = 1; i < str.size(); ++i ) {
		    if ( str[i] != str[i-1] )    num++;
		}
		long long ans = 0, c = 1;
		if ( num == 1 ) {
		    for ( int i = str.size()-1; i >= 0; --i ) {
		        ans += 1*c;
			    c = c*2;
		    }
			printf("Case #%d: ", ++cnt);
		cout << ans << endl;
		continue;
		}
		int flag[105];
		mset(flag, 0xff);
		for ( int i = 0; i < num; ++i ) {
			int t;
			if ( i == 0 )    t = 1;
			else if ( i == 1 )    t = 0;
			else t = i;
			int k;
		    for ( int j = 0; j < s.size(); ++j )
				if ( flag[j] == -1 )  {  flag[j] = t; k = j; break; }
			for ( int j = k+1; j < s.size(); ++j ) {
			    if ( s[j] == s[k] )   { flag[j] = t;  }
			}
		}
		//for ( int i = 0; i < s.size(); ++i )
		//	cout << flag[i] << endl;
		//cout << endl;
		//long long ans = 0, c = 1;
		for ( int i = str.size()-1; i >= 0; --i ) {
		    ans += flag[i]*c;
			c = c*num;
		}
		printf("Case #%d: ", ++cnt);
		cout << ans << endl;
	}
	return 0;
}
