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

int num[20];

int main()
{
	freopen("1.txt", "w", stdout);
	int n, cnd = 0;
	cin >> n;
	getchar();
	while ( n-- ) {
	    string s;
		getline(cin, s);
        mset(num, 0);
		for ( int i = 0; i < s.size(); ++i ) {
		    if ( s[i] == 'w' )    num[0]=(num[0]+1)%10000;
			if ( s[i] == 'e' )    num[1]+=num[0],num[6]+=num[5], num[14]+=num[13];
			if ( s[i] == 'l' )    num[2]+=num[1];
			if ( s[i] == 'c' )    num[3]+=num[2], num[11]+=num[10];
			if ( s[i] == 'o' )    num[4]+=num[3], num[9]+=num[8], num[12]+=num[11];
			if ( s[i] == 'm' )    num[5]+=num[4], num[18]+=num[17];
			if ( s[i] == ' ' )    num[7]+=num[6], num[10]+=num[9], num[15]+=num[14];
			if ( s[i] == 't' )    num[8]+=num[7];
            if ( s[i] == 'd' )    num[13]+=num[12];
			if ( s[i] == 'j' )    num[16]+=num[15];
			if ( s[i] == 'a' )    num[17]+=num[16];
			for ( int i = 0; i < 19; ++i )
				num[i] = num[i]%10000;
		}
		printf("Case #%d: %04d\n", ++cnd, num[18]);
	}
	return 0;
}
