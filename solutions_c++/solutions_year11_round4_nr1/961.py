//#pragma comment(linker, "/STACK:100000000")

#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cmath>
#include <ctime>

using namespace std;

#define sqr(a) ((a)*(a))
#define ab(a) (((a)>0)?(a) : (-(a)))
#define dist2(x1, y1, x2, y2) (sqr((x1)-(x2)) + sqr((y1)-(y2)))
#define PB push_back
#define SZ size()
#define ALL(a) (a).begin(),(a).end()
#define mset(a, val) memset(a, val, sizeof(a))
#define UNIQUE(p) sort(ALL(p)), p.resize( (int)(unique(ALL(p)) - p.begin()) )

#define pii pair < int, int >
#define pdd pair < double, double >
#define MP make_pair
#define X first
#define Y second

//#define INF 1000000000

//#define ll long long int
//#define INF ( ((ll)1) << 60 )


//////////////////////////////// GRAPHS ///////////////////////////////

//int di[] = {-1,0,1,0   ,   -1,1,1,-1};
//int dj[] = {0,1,0,-1   ,   1,1,-1,-1};

//#define inr(i,j)  ( 0 <= (i) && (i) < n && 0 <= (j) && (j) < n )   // square
//#define inr(i,j)  ( 0 <= (i) && (i) < n && 0 <= (j) && (j) < m )   // rectangular



//////////////////////////////// GEOMETRY//////////////////////////////

//#define mpi 3.1415926535897932384626433832795


//////////////////////////////// STRINGS ///////////////////////////////

//inline bool isc ( char c ) { return ( 'a' <= c && c <= 'z' || 'A' <= c && c <= 'Z' ); }
//inline bool isd ( char c ) { return '0' <= c && c <= '9'; }
//inline char tol ( char c ) { if ( 'A' <= c && c <= 'Z' ) c = c - 'A' + 'a'; return c; }
//inline char tou ( char c ) { if ( 'a' <= c && c <= 'z' ) c = c - 'a' + 'A'; return c; }

class CMP
{
public:
	bool operator()(pair < double, pii > & A, pair < double, pii > & B) const
	{
		if (A.Y.Y != B.Y.Y) return A.Y.Y < B.Y.Y;
		return A < B;
	}
} cmp;

int main () {
	int i, j, CAS;
	int X, S, R, n;
	double t;

	scanf("%d", &CAS);

	for (int cas = 1; cas <= CAS; cas++) {
		vector < pair < pii, int > > w;
		vector < pair < double, pii > > a;

		scanf("%d%d%d%lf%d", &X, &S, &R, &t, &n);
		for (i = 0; i < n; ++i)
		{
			int b, e, ww;
			scanf("%d%d%d", &b, &e, &ww);
			w.PB( MP( MP(b, e), ww ) );
		}

		sort(ALL(w));

		int cur = 0;

		for (i = 0; i < n; ++i)
		{
			if (cur < w[i].X.X)
			{
				pii temp1 = MP( w[i].X.X - cur, S );
				a.PB( MP( (double)temp1.X / (double)temp1.Y, temp1) );
			}

			pii temp = MP( w[i].X.Y - w[i].X.X, w[i].Y + S );
			a.PB( MP( (double)temp.X / (double)temp.Y, temp) );

			cur = w[i].X.Y;
		}

		if (cur < X)
		{
			pii temp1 = MP( X - cur, S );
			a.PB( MP( (double)temp1.X / (double)temp1.Y, temp1) );
		}

		sort(ALL(a), cmp);
		// sort(ALL(a), greater < pair < double, pii > >());

		double res = 0;
		double realSpeed;
		double canDoInTime;
		double distDone;
		double distWalk;

		for (i = 0; i < a.SZ; ++i)
		{
			realSpeed = a[i].Y.Y - S + R;
			canDoInTime = (double)a[i].Y.X / realSpeed;
			if (canDoInTime < t + 1e-9)
			{
				t -= canDoInTime;
				res += canDoInTime;
			}
			else
			{
				distDone = t * realSpeed;
				distWalk = (double)a[i].Y.X - distDone;
				res += t;
				res += distWalk / a[i].Y.Y;
				t = 0.0;
			}
		}
		
		printf("Case #%d: %.9lf\n", cas, res);
		cerr << cas << "\n";
	}

	cerr << "clock(): " << clock() << "\n";

	return 0;
}
