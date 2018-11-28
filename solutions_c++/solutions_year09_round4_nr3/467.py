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

//#define pii pair < int, int >
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

#define ll long long int

#define pii pair < ll , ll >
#define MP make_pair
#define X first
#define Y second

bool betw ( pii p1, pii p2, pii p3 ) {
	if ( min(p1.X, p2.X) <= p3.X && p3.X <= max(p1.X, p2.X) &&
		 min(p1.Y, p2.Y) <= p3.Y && p3.Y <= max(p1.Y, p2.Y) ) return true;
	return false;
}

ll vp (pii p1, pii p2, pii p3) {
	return ( (p3.X - p1.X)*(p2.Y-p1.Y) - (p3.Y - p1.Y)*(p2.X-p1.X) );
}

bool intersect( pii P0, pii P1, pii P2, pii P3) {
	ll d1, d2, d3, d4;
	d1 = vp( P0, P1, P2 );
	d2 = vp( P0, P1, P3 );

	d3 = vp( P2, P3, P0 );
	d4 = vp( P2, P3, P1 );

	if ( (d1 > 0 && d2 < 0 || d1 < 0 && d2 > 0) &&
		 (d3 > 0 && d4 < 0 || d3 < 0 && d4 > 0) ) return true;

	if (d1 == 0 && betw( P0, P1, P2 )) return true;
	if (d2 == 0 && betw( P0, P1, P3 )) return true;
	if (d3 == 0 && betw( P2, P3, P0 )) return true;
	if (d4 == 0 && betw( P2, P3, P1 )) return true;

	return false;
}

#define N 111

ll p[N][N];
bool a[N][N];
int n, m;

int cntbits(int x) {
	int res = 0;
	while (x>0) { ++res; x -= (x&-x); }
	return res;
}

bool f (int I, int J) {
	int i, j;
	for (i = 0; i < m-1; ++i) {
		for (j = 0; j < m-1; ++j) {
			if (intersect( MP(i, p[I][i]), MP(i+1, p[I][i+1]), MP(j, p[J][j]), MP(j+1, p[J][j+1]) )) {
				return true;
			}
		}
	}
	return false;
}

int dp[1<<16];

int f (int x) {
	if (dp[x] != -1) return dp[x];
	if (cntbits(x) == 1) return dp[x] = 1;

	int y, res = 100, i, j;
	for (y = (x-1)&x; y > 0; y = (y-1)&x) {
		int A = y, B = x-y;
		if (f(A) == 1 && f(B) == 1) {
			bool ok = true;
			for (i = 0; i < n; ++i) if (A & (1<<i)) {
				for (j = 0; j < n; ++j) if (B & (1<<j)) {
					if (a[i][j]) {
						ok = false;
						break;
					}
				}
				if (!ok) break;
			}
			if (ok) return dp[x] = 1;
		}		
		res = min(res, f(A) + f(B));
	}
	return dp[x] = res;
}

int main () {
	int i, j, CAS;

	scanf("%d", &CAS);

	for (int cas = 1; cas <= CAS; cas++) {

		scanf("%d%d", &n, &m);

		mset(a,0);
		mset(p,0);

		for (i = 0; i < n; ++i) for (j = 0; j < m; ++j) scanf("%lld", &p[i][j]);

		for (i = 0; i < n; ++i) for (j = i+1; j < n; ++j) {
			a[i][j] = a[j][i] = f(i,j);
		}

		mset(dp,-1);

		int res = f((1<<n)-1);
		
		printf("Case #%d: %d\n", cas, res);
		cerr << cas << "\n";
	}

	cerr << "clock(): " << clock() << "\n";

	return 0;
}


