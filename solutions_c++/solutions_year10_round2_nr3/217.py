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

#define M 100003

/*

inline bool verify(int *a, int len, int x, int mask)
{
	int ind = len;

	if (a[ind-1] != x) return false;

	while (ind > 1) //???
	{
		x = ind;
//		if (mask & (1<<(ind-2)))

		while (ind > 0 && a[ind-1] != x) --ind;
		if (ind <= 0) return false;
	}
	if (ind == 1) return true;
	return false;
}

int precalc(int x)
{
	int n = x - 2;
	int a[30];
	int len = 0, i, mask, res = 0;

	for (mask = 0; mask < (1<<n); ++mask)
	{
		len = 0;
		for (i = 0; i < n; ++i) if (mask & (1<<i))
		{
			a[len++] = i + 2;
		}
		a[len++] = x;

		if (verify(a, len, x, mask))
		{
			++res;
			res %= M;
		}
	}

	return res;
}

void doPrecalc()
{
	printf("int val[] = {0, 0, 1, ");
	for (int i = 3; i <= 25; ++i)
	{
		printf("%d", precalc(i));
		if (i < 25) printf(", ");
	}
	printf("};\n");
}

int val[] = {0, 0, 1, 2, 3, 5, 8, 14, 24, 43, 77, 140, 256, 472, 874, 1628, 3045, 5719, 10780, 20388, 38674, 73562, 40265, 68060, 13335, 84884};
*/

#define N 511

int F[N][N];

int main () {
	int i, j, k, x, CAS;

	//doPrecalc();

	// Precalc
	mset(F,0);
	for (i = 0; i < N; ++i) F[0][i] = 1;

	for (j = 1; j < N; ++j)
	{
		for (i = 1; i < N; ++i) 
		{
			for (k = 1; k <= j && i-k >= 0; ++k)
			{
				F[i][j] += F[i-k][j];
				F[i][j] %= M;
			}
		}
	}

	scanf("%d", &CAS);

	for (int cas = 1; cas <= CAS; cas++) {
		scanf("%d", &x);

		int res = 0;

		for (i = x-1, j = 0; i >= 0; --i, ++j)
		{
			res += F[i][j];
			res %= M;
		}
		
		printf("Case #%d: %d\n", cas, res);
		//cerr << cas << "\n";
	}

	//cerr << "clock(): " << clock() << "\n";

	return 0;
}


