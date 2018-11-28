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

struct point {
    double x, y, z, vx, vy, vz;
};

point p[505];

int main()
{
	freopen("1.txt", "w", stdout);
	int T, cnd = 0;
	cin >> T;
	while ( T-- ) {
	    int n;
		cin >> n;
		for ( int i = 0; i < n; ++i )
			cin>>p[i].x>>p[i].y>>p[i].z>>p[i].vx>>p[i].vy>>p[i].vz;
		double cx=0, cy=0, cz=0, Vx=0, Vy=0, Vz=0;
		for ( int i = 0; i < n; ++i ) {
		    cx += p[i].x, Vx += p[i].vx;
			cy += p[i].y, Vy += p[i].vy;
			cz += p[i].z, Vz += p[i].vz;
		}
		cx /= n, cy /= n, cz /= n;
		Vx /= n, Vy /= n, Vz /= n;
		double a, b, c;
		a = Vx*Vx+Vy*Vy+Vz*Vz, b = Vx*cx+Vy*cy+Vz*cz, c = cx*cx+cy*cy+cz*cz;
		double t, dis;
		if ( a == 0 ) {   
			t = 0;
			dis = cx*cx+cy*cy+cz*cz;
			dis = sqrt(dis);
			printf("Case #%d: %.8lf %.8lf\n", ++cnd, dis, t);
			continue;
		}
		else { 
			t = -b/a;
		    if ( t < 0 )    t = 0;
		}
		dis = (cx+Vx*t)*(cx+Vx*t)+(cy+Vy*t)*(cy+Vy*t)+(cz+Vz*t)*(cz+Vz*t);
		dis = sqrt(dis);
		printf("Case #%d: %.8lf %.8lf\n", ++cnd, dis, t);
	}
	return 0;
}
