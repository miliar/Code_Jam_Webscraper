#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cfloat>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

#define bublic public
#define clr(x) memset((x), 0, sizeof(x))
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define pf push_front
#define mp make_pair
#define popf pop_front
#define popb pop_back
#define sz size()
#define fst first
#define snd second
#define It(x) x::iterator
#define CIt(x) x::const_iterator
#define For(i, st, en) for(int i=(st); i<=(en); i++)
#define Ford(i, st, en) for(int i=(st); i>=(en); i--)
#define forn(i, n) for(int i=0; i<(int)(n); i++)
#define ford(i, n) for(int i=(n)-1; i>=0; i--)

template <class _T> inline _T sqr(const _T& x) { return x * x; }
template <class _T> inline string tostr(const _T& a) { ostringstream os(""); os << a; return os.str(); }
template <class _T> inline istream& operator << (istream& is, const _T& a) { is.putback(a); return is; }

typedef long double ld;

// Constants
const ld PI = 3.1415926535897932384626433832795;
const ld EPS = 1e-12;

// Types
typedef signed   long long i64;
typedef unsigned long long u64;
typedef set < int > SI;
typedef vector < ld > VD;
typedef vector < int > VI;
typedef vector < bool > VB;
typedef vector < string > VS;
typedef map < string, int > MSI;
typedef pair < int, int > PII;

struct tpoint
{
	ld x,y,z,vx,vy,vz;
};

int n,t;
tpoint a[1024];

int main()
{
#ifdef HOME
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif
	cout << setiosflags(ios::fixed) << setprecision(10);

	scanf("%d",&t);
	forn(tt,t)
	{
		printf("Case #%d: ",tt+1);

		scanf("%d",&n);
		forn(i,n)
		{
			int x,y,z,vx,vy,vz;
			scanf("%d%d%d%d%d%d",&x,&y,&z,&vx,&vy,&vz);
			a[i].x=x;
			a[i].y=y;
			a[i].z=z;
			a[i].vx=vx;
			a[i].vy=vy;
			a[i].vz=vz;
		}

		ld t1=0.0, t2=10000000.0;

		while (fabs(t1-t2)>EPS)
		{
//			cerr << t1 << " " << t2<<endl;
//			if (fabs(t1-t2)<1e-5) break;
			ld xc1=0.0,yc1=0.0,zc1=0.0;
			forn(i,n)
			{
				xc1+=a[i].x+a[i].vx*t1;
				yc1+=a[i].y+a[i].vy*t1;
				zc1+=a[i].z+a[i].vz*t1;
			}
			xc1/=(n*1.0);
			yc1/=(n*1.0);
			zc1/=(n*1.0);

			ld xc2=0.0,yc2=0.0,zc2=0.0;
			forn(i,n)
			{
				xc2+=a[i].x+a[i].vx*t2;
				yc2+=a[i].y+a[i].vy*t2;
				zc2+=a[i].z+a[i].vz*t2;
			}
			xc2/=(n*1.0);
			yc2/=(n*1.0);
			zc2/=(n*1.0);

			ld t3=(t1+t2)/2.0;
			ld xc3=0.0,yc3=0.0,zc3=0.0;
			forn(i,n)
			{
				xc3+=a[i].x+a[i].vx*t3;
				yc3+=a[i].y+a[i].vy*t3;
				zc3+=a[i].z+a[i].vz*t3;
			}
			xc3/=(n*1.0);
			yc3/=(n*1.0);
			zc3/=(n*1.0);

			ld dd1=(xc1)*(xc1)+(yc1)*(yc1)+(zc1)*(zc1);
			ld dd2=(xc2)*(xc2)+(yc2)*(yc2)+(zc2)*(zc2);
			ld dd3=(xc3)*(xc3)+(yc3)*(yc3)+(zc3)*(zc3);
			if (dd2>dd1+EPS && dd2>dd3+EPS)
			{
				t2=t3;
			} else
			{
				t1=t3;
			}
/*
			if (dd2>dd1+EPS && dd2>dd3+EPS)
			{
				t2=t3;
			}
*/
		}
//		t1=0.0;
		t2=0.0;
		ld xc1=0.0,yc1=0.0,zc1=0.0;
		forn(i,n)
		{
			xc1+=a[i].x+a[i].vx*t1;
			yc1+=a[i].y+a[i].vy*t1;
			zc1+=a[i].z+a[i].vz*t1;
		}
		xc1/=(n*1.0);
		yc1/=(n*1.0);
		zc1/=(n*1.0);
		ld xc2=0.0,yc2=0.0,zc2=0.0;
		forn(i,n)
		{
			xc2+=a[i].x+a[i].vx*t2;
			yc2+=a[i].y+a[i].vy*t2;
			zc2+=a[i].z+a[i].vz*t2;
		}
		xc2/=(n*1.0);
		yc2/=(n*1.0);
		zc2/=(n*1.0);

		ld dd1=sqrt((xc1)*(xc1)+(yc1)*(yc1)+(zc1)*(zc1));
		ld dd2=sqrt((xc2)*(xc2)+(yc2)*(yc2)+(zc2)*(zc2));
		if (fabs(dd1 - dd2)<1e-7) cout << dd1 << " " << t2<< endl;
		else cout << dd1 << " " << t1<< endl;


	}

	return 0;
}
