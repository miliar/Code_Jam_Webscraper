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

#define N 200

int a[N][N], k, n;
int b[N][N], c[N][N], d[N][N];

bool check(int di, int dj, int sz)
{
	int i, j, ii, jj;
	for (i = 0; i < sz; ++i) for (j = 0; j < sz-i; ++j)
	{
		ii = sz-1-j;
		jj = sz-1-i;
		if (0 <= i-di && i-di < n && 0 <= j-dj && j-dj < n &&
			0 <= ii-di && ii-di < n && 0 <= jj-dj && jj-dj < n) if (d[i][j] != d[ii][jj]) return false;
	}
	for (i = 0; i < sz; ++i) for (j = 0; j < i; ++j)
	{
		ii = j;
		jj = i;
		if (0 <= i-di && i-di < n && 0 <= j-dj && j-dj < n &&
			0 <= ii-di && ii-di < n && 0 <= jj-dj && jj-dj < n) if (d[i][j] != d[ii][jj]) return false;
	}
	return true;
}


bool check(int sz)
{
	int i, j, ii, jj;
	int di = 0, dj = 0;
	for (di = 0; di+n <= sz; ++di) for (dj = 0; /*dj+n <= sz*/ dj < 1; ++dj)
	{
		for (i = 0; i < n; ++i) for (j = 0; j < n; ++j) d[i+di][j+dj] = b[i][j];
		if (check(di, dj, sz)) {
			return true;
		}
	}
	/*
	for (i = 0; i < sz; ++i) for (j = 0; j < sz-i; ++j)
	{
		ii = sz-1-j;
		jj = sz-1-i;
		if (ii < n && jj < n) if (b[i][j] != b[ii][jj]) return false;
	}
	for (i = 0; i < sz; ++i) for (j = 0; j < i; ++j)
	{
		ii = j;
		jj = i;
		if (ii < n && jj < n) if (b[i][j] != b[ii][jj]) return false;
	}
	return true;
	*/
	return false;
	
}



void rotate()
{
	int i, j;
	mset(c,0);
	memcpy(c, b, sizeof(b));
	mset(b,0);
	for (i = 0; i < n; ++i) {
		for (j = 0; j < n; ++j) {
			b[n-1-j][i] = c[i][j];
			//b[i][j] = c[j][n-1-i];
		}
	}
}

int solve()
{
	int i, j;

	if (n == 1) return n;

	mset(b,0);

	for (i = 0; i < n; ++i) for (j = 0; j < n; ++j) b[i][j] = a[i][j];
	if (check(n)) return n;

	for (int sz = n+1; sz <= n*3+3; ++sz)
	{
		for (i = 0; i < n; ++i) for (j = 0; j < n; ++j) b[i][j] = a[i][j];
		if (check(sz)) return sz;
		rotate();
		if (check(sz)) return sz;
		rotate();
		if (check(sz)) return sz;
		rotate();
		if (check(sz)) return sz;
	}

	//return n+n-1;
	return 1000;
}

int main () {
	int i, j, CAS, x;

	scanf("%d", &CAS);

	for (int cas = 1; cas <= CAS; cas++) {
		mset(a,0);

		scanf("%d", &k);

		n = k;

		for (i = 0; i < 2*k-1; ++i)
		{
			int sz = (i < k ? i+1 : 2*k-1-i);
			int row = (i < k ? i : k-1);
			for (j = 0; j < sz; ++j)
			{
				int col = (i < k ? j : j+(i-k+1));
				scanf("%d", &x);
				a[row--][col] = x;
			}
		}

		int res = solve();
		res -= n;
		res = res*n*2 + res*res;
		
		printf("Case #%d: %d\n", cas, res);
		cerr << cas << "\n";
	}

	cerr << "clock(): " << clock() << "\n";

	return 0;
}


