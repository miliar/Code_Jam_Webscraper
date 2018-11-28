#include <cstring>
#include <string.h>
#include <conio.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>

using namespace std;

#define pb push_back
#define ALL(v) v.begin(),v.end()
#define RALL(v) v.rbegin(),v.rend()
#define SZ(c) (c).size()
#define FOR(i,a,b) for(int _n(b),i(a);i<_n;i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(__typeof(c.begin()) it=c.begin();it!=c.end();++it)
#define REP(i,n) FOR(i,0,n)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define MEM(a,b) memset(a,b,sizeof(a))
#define MP make_pair
#define DOT(a,b) ((conj(a)*(b)).X)
#define X real()
#define Y imag()
#define length(V) (hypot((V).X,(V).Y))
#define vect(a,b) ((b)-(a))
#define cross(a,b) ((conj(a)*(b)).imag())
#define normalize(v) ((v)/length(v))
#define rotate(p,about,theta) ((p-about)*exp(point(0,theta))+about)
#define pointEqu(a,b) (comp(a.X,b.X)==0 && comp(a.Y,b.Y)==0)

typedef stringstream ss;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<vector<int> > vii;
typedef long long ll;
typedef long double ld;
typedef complex<double> point;
typedef pair<point, point> segment;
typedef pair<double, point> circle;
typedef vector<point> polygon;

const long double PI = 3.1415926535897932384626433832795028841968;
const double eps = 1e-9;
int di[] = { 0, -1, -1, -1, 0, 1, 1, 1 };
int dj[] = { -1, -1, 0, 1, 1, 1, 0, -1 };
int diK[] = { -2, -2, -1, 1, 2, 2, 1, -1 };
int djK[] = { -1, 1, 2, 2, 1, -1, -2, -2 };

inline int comp(const double &a, const double &b) 
{
	if (fabs(a - b) < eps)
		return 0;
	return a > b ? 1 : -1;
}

int I, J;
inline bool val(const int &i, const int &j) {
	if (i < 0 || j < 0 || i >= I || j >= J)
		return false;
	return true;
}

//#define TEST
//#define SMALL
#define LARGE

int main() 
{
#ifdef TEST
	freopen("A.txt", "r", stdin);
#endif
#ifdef SMALL
	freopen("A-small-attempt2.in","r",stdin);
	freopen("A-small.out","w+",stdout);
#endif
#ifdef LARGE
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w+",stdout);
#endif
	int T;
	cin >> T;
	REP(test,T)	{
		//code
		cout << "Case #" << test + 1 << ": ";
		int R, C, res=1;
		char c;
		cin >> R >> C;
		vii a(R,vi(C));
		REP(i,R) {
			 REP(j,C){
				 cin >> c;
				 if (c == '.' && a[i][j]>0) {
						 res = 0;

				 } else if (c=='#'){
						if (a[i][j] == 0) {
							if ((i+1 == R) || (j+1==C)) {
								res = 0;
							} else {
								a[i][j] = 1; a[i][j+1] = 2; a[i+1][j]=2; a[i+1][j+1]=1;
							}
						}
				}
			}
		}
		if (res==1) {
			REP(i,R){
				cout << endl;
				REP(j,C) 
					if(a[i][j]==0) cout <<'.'; else if(a[i][j] == 1) cout << '/'; else cout << '\\';
			}
		} else cout << endl << "Impossible";
		cout << endl;
	}
#ifdef TEST
	getch();
#endif
	return 0;
}